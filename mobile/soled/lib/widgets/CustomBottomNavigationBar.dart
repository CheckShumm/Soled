import 'package:bottom_navy_bar/bottom_navy_bar.dart';
import 'package:flutter/material.dart';

class CustomBottomNavigationBar extends StatefulWidget {
  final int currentIndex;
  ValueChanged<int> onTap;

  final backgroundColor = Colors.white;
  final tabColor = Colors.blue[900];

  CustomBottomNavigationBar({Key key, @required this.currentIndex, @required this.onTap}) : super(key: key);

  @override
  _CustomBottomNavigationBarState createState() =>
      _CustomBottomNavigationBarState();
}

class _CustomBottomNavigationBarState extends State<CustomBottomNavigationBar> {
  @override
  Widget build(BuildContext context) {
    return BottomNavyBar(
      backgroundColor: this.widget.backgroundColor,
      selectedIndex: this.widget.currentIndex,
      showElevation: false,
      onItemSelected: (index) => this.widget.onTap(index),
      items: [
        BottomNavyBarItem(
          icon: Icon(Icons.dashboard),
          title: Text('Gallery'),
          activeColor: this.widget.tabColor,
        ),
        BottomNavyBarItem(
          icon: Icon(Icons.favorite),
          title: Text('Favorites'),
          activeColor: this.widget.tabColor,
        ),
        BottomNavyBarItem(
            icon: Icon(Icons.search),
            title: Text('Search'),
            activeColor: this.widget.tabColor
        ),
        BottomNavyBarItem(
            icon: Icon(Icons.assessment),
            title: Text('Data'),
            activeColor: this.widget.tabColor
        ),
        BottomNavyBarItem(
            icon: Icon(Icons.person),
            title: Text('Profile'),
            activeColor: this.widget.tabColor
        ),
      ],
    );
  }
}
