import 'package:flutter/material.dart';

class BookingPage extends StatelessWidget {
  final List<String> courts = [
    "Tennis",
    "Basketball",
    "Football",
    "Volleyball"
  ];
  final List<String> timeSlots = ["8:00 AM", "10:00 AM", "12:00 PM", "2:00 PM"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Book a Court")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text("Select a Court:", style: TextStyle(fontSize: 18)),
            const SizedBox(height: 10),
            DropdownButtonFormField(
              items: courts.map((court) {
                return DropdownMenuItem(value: court, child: Text(court));
              }).toList(),
              onChanged: (value) {
                // Handle court selection
              },
              decoration: const InputDecoration(border: OutlineInputBorder()),
            ),
            const SizedBox(height: 20),
            const Text("Select a Time Slot:", style: TextStyle(fontSize: 18)),
            const SizedBox(height: 10),
            DropdownButtonFormField(
              items: timeSlots.map((slot) {
                return DropdownMenuItem(value: slot, child: Text(slot));
              }).toList(),
              onChanged: (value) {
                // Handle time slot selection
              },
              decoration: const InputDecoration(border: OutlineInputBorder()),
            ),
            const SizedBox(height: 30),
            ElevatedButton(
              onPressed: () {
                // Add booking confirmation logic here
                Navigator.pushNamed(context, '/confirmation');
              },
              child: const Text("Confirm Booking"),
            ),
          ],
        ),
      ),
    );
  }
}
