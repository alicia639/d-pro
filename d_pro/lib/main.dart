import "package:flutter/material.dart";

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        primaryColor: Colors.blue[800],
      ),
      home: Scaffold(
        body: SingleChildScrollView(
          child: Container(
            padding: EdgeInsets.symmetric(horizontal: 40, vertical: 70),
            child: Column(
              children: [
                Image.asset(
                  "images/creepy.jpeg",
                  width: 300,
                  height: 300,
                ),
                Text("D-PRO"),
                Text("Self Dental Checkup at Home"),
                TextField(
                  decoration: InputDecoration(
                    helperText: 'Enter Full Name',
                  ),
                ),
                TextField(
                  decoration: InputDecoration(
                    helperText: 'Enter Full Name',
                  ),
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
      ),
    );
  }
}
