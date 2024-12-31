import 'package:flutter/material.dart';
import 'package:sports_court_reservation_system/booking_confirmed.dart';
import 'package:sports_court_reservation_system/signup_page.dart';
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
        '/login': (context) => const LoginPage(),
        '/signup': (context) => const SignUpPage(), // Placeholder
        '/booking': (context) => BookingPage(),
        '/dashboard': (context) => AdminDashboard(),
        '/confirmation': (context) =>
            const BookingConfirmedPage(), // Placeholder
      },
    );
  }
}
