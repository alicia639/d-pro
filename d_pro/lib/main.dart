import "package:flutter/material.dart";

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
      home: SignUpPage(),
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
