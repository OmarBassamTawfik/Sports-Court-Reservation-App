import 'package:flutter/material.dart';
import 'landing_page.dart';
import 'login_page.dart';
import 'booking_page.dart';
import 'admin_dashboard.dart';

void main() {
  runApp(const SportsCourtApp());
}

class SportsCourtApp extends StatelessWidget {
  const SportsCourtApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      initialRoute: '/',
      routes: {
        '/': (context) => const LandingPage(),
        '/login': (context) => LoginPage(),
        '/signup': (context) => const Scaffold(
            body: Center(child: Text("Signup Page"))), // Placeholder
        '/booking': (context) => BookingPage(),
        '/dashboard': (context) => AdminDashboard(),
        '/confirmation': (context) => const Scaffold(
            body: Center(child: Text("Booking Confirmed"))), // Placeholder
      },
    );
  }
}
