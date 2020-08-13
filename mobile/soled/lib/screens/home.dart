import 'package:bottom_navy_bar/bottom_navy_bar.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:soled/widgets/CustomBottomNavigationBar.dart';

class Home extends StatefulWidget {
  Home({Key key}) : super(key: key);

  final String title = 'SOLED';

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  int _selectedIndex = 2;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.white,
        iconTheme: new IconThemeData(color: Colors.blue[900]),
        title: Text(widget.title, style: TextStyle(fontSize: 20.0, color: Colors.blue[900], letterSpacing: 5.0)),
        centerTitle: true,
        actions: <Widget>[
          Padding(
            padding: const EdgeInsets.only(right: 16.0),
            child: Icon(Icons.notifications),
          ),
        ],
        elevation: 0.0,
      ),
      drawer: Drawer(),
      body: Stack(
        children: <Widget>[
         
        ],
      ),
      bottomNavigationBar: CustomBottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: (index) => {
          setState(() {
            _selectedIndex = index;
            print(index);
          })
        }
      )
    );
  }
}