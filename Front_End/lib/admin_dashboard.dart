import 'package:flutter/material.dart';

class AdminDashboard extends StatelessWidget {
  final List<Map<String, String>> bookings = [
    {"Court": "Tennis", "Time": "8:00 AM", "User": "John Doe"},
    {"Court": "Basketball", "Time": "10:00 AM", "User": "Jane Smith"},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Admin Dashboard")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text("Bookings:", style: TextStyle(fontSize: 18)),
            const SizedBox(height: 10),
            Expanded(
              child: ListView.builder(
                itemCount: bookings.length,
                itemBuilder: (context, index) {
                  final booking = bookings[index];
                  return Card(
                    child: ListTile(
                      title: Text("Court: ${booking['Court']}"),
                      subtitle: Text(
                          "Time: ${booking['Time']}\nUser: ${booking['User']}"),
                      trailing: IconButton(
                        icon: const Icon(Icons.cancel),
                        onPressed: () {
                          // Handle cancellation logic
                        },
                      ),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
