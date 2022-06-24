import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:frontend/models/todo.dart';
import 'package:frontend/widgets/appbar.dart';
import 'package:frontend/widgets/todo_container.dart';
import 'api.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  List<Todo> myTodos = [];
  @override
  void fetchData() async {
    try {
      http.Response response = await http.get(Uri.parse(api));
      var data = json.decode(response.body);

      // var data = response.body;
      // json.decode(data);
      // print(data);
      // print(response.body.runtimeType);
      // print(data.runtimeType);
      data.forEach((todo) {
        // myTodos.add(todo);
        Todo t = Todo(
            id: todo['id'],
            title: todo['title'],
            body: todo['body'],
            date: todo['date']);
        myTodos.add(t);
      });

      print(myTodos.length);
    } catch (e) {
      print("Error is $e");
    }
  }

  void initState() {
    fetchData();
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: appBar1(),
      backgroundColor: const Color.fromARGB(255, 78, 128, 148),
      body: ListView(
        children: myTodos.map((e) {
          return  TodoContainer(
              id: e.id, title: e.title, body: e.body, date: e.date);
        }).toList(),
      ),
    );
  }
}
