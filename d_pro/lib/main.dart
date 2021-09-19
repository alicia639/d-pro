import "package:flutter/material.dart";
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primaryColor: Colors.blue[800],
      ),
      home: ImageUploadPage(),
    );
  }
}

class SignUpPage extends StatelessWidget {
  const SignUpPage({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
          width: double.infinity,
          padding: EdgeInsets.symmetric(horizontal: 40, vertical: 40),
          child: Column(
            children: [
              Image.asset(
                "images/signup.png",
                width: 300,
                height: 300,
              ),
              Text(
                "D-PRO",
                style: TextStyle(
                  color: Colors.blue[800],
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                "Self Dental Checkup at Home",
                style: TextStyle(
                  color: Colors.blue[800],
                ),
              ),
              SizedBox(
                width: 300,
                child: TextField(
                  decoration: InputDecoration(
                    helperText: 'Enter Full Name',
                  ),
                ),
              ),
              SizedBox(
                width: 300,
                child: TextField(
                  decoration: InputDecoration(
                    helperText: 'Enter Full Name',
                  ),
                ),
              ),
              SizedBox(
                height: 40,
              ),
              ElevatedButton(
                onPressed: () {},
                child: Text("Sign Up"),
                style: ElevatedButton.styleFrom(minimumSize: Size(300, 40)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class ImageUploadPage extends StatefulWidget {
  const ImageUploadPage({Key? key}) : super(key: key);

  @override
  _ImageUploadPageState createState() => _ImageUploadPageState();
}

class _ImageUploadPageState extends State<ImageUploadPage> {
  @override
  File? image;
  Future pickImage() async {
    try {
      final image = await ImagePicker().pickImage(source: ImageSource.gallery);

      if (image == null) return;

      final tempImage = File(image.path);
      setState(() {
        this.image = tempImage;
      });
    } on PlatformException catch (e) {
      print("Failed to pick an image: $e");
    }
  }

  Widget build(BuildContext context) {
    return Container(
        child: Column(
      children: [
        Container(
          child:
              image != null ? Image.file(image!) : Image.asset("creepy.jpeg"),
          width: 300,
          height: 300,
        ),
        ElevatedButton(
            onPressed: () {
              pickImage();
            },
            child: Text("Pick an image"))
      ],
    ));
  }
}
