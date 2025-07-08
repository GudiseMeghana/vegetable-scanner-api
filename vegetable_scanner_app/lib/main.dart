import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'package:http_parser/http_parser.dart';

void main() => runApp(VegetableScannerApp());

class VegetableScannerApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Vegetable Scanner',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: 'Arial',
        primaryColor: Colors.green,
        scaffoldBackgroundColor: Color(0xFFF4FFF3),
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            minimumSize: Size(double.infinity, 50),
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
            textStyle: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
          ),
        ),
      ),
      home: VegetableScannerPage(),
    );
  }
}

class VegetableScannerPage extends StatefulWidget {
  @override
  _VegetableScannerPageState createState() => _VegetableScannerPageState();
}

class _VegetableScannerPageState extends State<VegetableScannerPage> {
  List<_ScannedItem> _scannedItems = [];
  File? _image;
  String _result = '';
  bool _loading = false;
  final ImagePicker _picker = ImagePicker();

  Future<void> _getImage(ImageSource source) async {
    final picked = await _picker.pickImage(source: source);
    if (picked != null) {
      setState(() {
        _image = File(picked.path);
        _result = '';
      });
      await _uploadImage(_image!, picked.name, picked.path);
    }
  }

  Future<void> _uploadImage(File imageFile, String imageName, String imagePath) async {
    setState(() => _loading = true);
    final uri = Uri.parse("https://vegetable-scanner-api.onrender.com/predict/");
    final request = http.MultipartRequest('POST', uri);
    request.files.add(await http.MultipartFile.fromPath(
      'file',
      imageFile.path,
      contentType: MediaType('image', 'jpeg'),
    ));

    try {
      final response = await request.send();
      final body = await response.stream.bytesToString();
      if (response.statusCode == 200) {
        final parsed = json.decode(body);
        final now = DateTime.now();
        final TextEditingController weightController = TextEditingController();
        await showDialog(
          context: context,
          builder: (context) => AlertDialog(
            title: Text('Enter Weight (kg)'),
            content: TextField(
              controller: weightController,
              keyboardType: TextInputType.numberWithOptions(decimal: true),
              decoration: InputDecoration(hintText: 'Weight in kg'),
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.of(context).pop(),
                child: Text('OK'),
              ),
            ],
          ),
        );
        final weight = weightController.text;
        setState(() {
          _scannedItems.add(_ScannedItem(
            sno: _scannedItems.length + 1,
            imageName: imageName,
            timestamp: now,
            description: parsed['vegetable'] ?? '',
            weight: weight,
            result: parsed,
            imagePath: imagePath,
          ));
        });
      }
      setState(() => _result = response.statusCode == 200 ? body : 'Error: ${response.statusCode}');
    } catch (e) {
      setState(() => _result = 'Error: $e');
    } finally {
      setState(() => _loading = false);
    }
  }

  void _generateReport() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Scanned Report'),
        content: SizedBox(
          width: MediaQuery.of(context).size.width * 0.9,
          height: 400,
          child: Scrollbar(
            thumbVisibility: true,
            child: SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: ConstrainedBox(
                constraints: BoxConstraints(minWidth: 600),
                child: SingleChildScrollView(
                  scrollDirection: Axis.vertical,
                  child: DataTable(
                    columns: const [
                      DataColumn(label: Text('Sno.')),
                      DataColumn(label: Text('Image')),
                      DataColumn(label: Text('Timestamp')),
                      DataColumn(label: Text('Description')),
                      DataColumn(label: Text('Weight')),
                    ],
                    rows: _scannedItems.map((item) => DataRow(cells: [
                      DataCell(Text(item.sno.toString())),
                      DataCell(Text(item.imageName)),
                      DataCell(Text(item.timestamp.toString())),
                      DataCell(Text(item.description)),
                      DataCell(Text(item.weight)),
                    ])).toList(),
                  ),
                ),
              ),
            ),
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text('Close'),
          ),
        ],
      ),
    );
  }

  Widget _buildGradientButton({required String text, required IconData icon, required VoidCallback onPressed, required List<Color> colors}) {
    return Container(
      width: double.infinity,
      margin: EdgeInsets.symmetric(vertical: 8),
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: colors),
        borderRadius: BorderRadius.circular(12),
      ),
      child: ElevatedButton.icon(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.transparent,
          shadowColor: Colors.transparent,
          foregroundColor: Colors.white,
        ),
        onPressed: onPressed,
        icon: Icon(icon),
        label: Text(text),
      ),
    );
  }

  Widget _buildResultCard() {
    try {
      final parsed = json.decode(_result);
      return Container(
        padding: EdgeInsets.all(16),
        margin: EdgeInsets.only(top: 20),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.9),
          borderRadius: BorderRadius.circular(16),
          boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 10)],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            _buildRow("Vegetable", parsed['vegetable']),
            _buildRow("Confidence", "${parsed['confidence']}%"),
            _buildRow("Product ID", parsed['product_id']),
            _buildRow("Price per Kg", "${parsed['price_per_kg']}"),
          ],
        ),
      );
    } catch (e) {
      return Container(
        padding: EdgeInsets.all(16),
        margin: EdgeInsets.only(top: 20),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.9),
          borderRadius: BorderRadius.circular(16),
          boxShadow: [BoxShadow(color: Colors.black12, blurRadius: 10)],
        ),
        child: Text(
          'Prediction: $_result',
          style: TextStyle(fontSize: 16),
        ),
      );
    }
  }

  Widget _buildRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Text(
            '$label: ',
            style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16),
          ),
          Expanded(
            child: Text(
              value,
              style: TextStyle(fontSize: 16),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Vegetable Scanner'),
        backgroundColor: Colors.green[700],
        centerTitle: true,
        actions: [
          if (_scannedItems.isNotEmpty)
            IconButton(
              icon: Icon(Icons.assignment),
              tooltip: 'Generate Report',
              onPressed: _generateReport,
            ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: SingleChildScrollView(
          child: Column(
            children: [
              _buildGradientButton(
                text: "Take a Photo",
                icon: Icons.camera_alt,
                colors: [Colors.green.shade700, Colors.green.shade400],
                onPressed: () => _getImage(ImageSource.camera),
              ),
              _buildGradientButton(
                text: "Upload from Gallery",
                icon: Icons.image,
                colors: [Colors.teal.shade600, Colors.teal.shade300],
                onPressed: () => _getImage(ImageSource.gallery),
              ),
              if (_scannedItems.isNotEmpty) ...[
                SizedBox(height: 20),
                Text('Scanned Items:', style: TextStyle(fontWeight: FontWeight.bold)),
                ListView.builder(
                  shrinkWrap: true,
                  physics: NeverScrollableScrollPhysics(),
                  itemCount: _scannedItems.length,
                  itemBuilder: (context, idx) {
                    final item = _scannedItems[idx];
                    return Card(
                      child: ListTile(
                        leading: Icon(Icons.image),
                        title: Text(item.description),
                        subtitle: Text('Weight: ${item.weight} kg\n${item.timestamp}'),
                        trailing: Text('Sno: ${item.sno}'),
                      ),
                    );
                  },
                ),
              ],
              if (_loading) Padding(
                padding: const EdgeInsets.only(top: 20),
                child: CircularProgressIndicator(color: Colors.green),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _ScannedItem {
  final int sno;
  final String imageName;
  final DateTime timestamp;
  final String description;
  final String weight;
  final Map result;
  final String imagePath;
  _ScannedItem({
    required this.sno,
    required this.imageName,
    required this.timestamp,
    required this.description,
    required this.weight,
    required this.result,
    required this.imagePath,
  });
}