
import 'package:flutter/material.dart';

class TodoContainer extends StatelessWidget {
  final int id;
  final String title;
  final String body;
  final String date;
     
  const TodoContainer({
    Key? key,
    required this.id,
    required this.title,
    required this.body,
    required this.date,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: Container(
        width: double.infinity,
        height: 120,
        decoration: const BoxDecoration(
              color:Colors.pink ,
              borderRadius: BorderRadius.all(Radius.circular(5)),
           ),
          child: Padding(padding: const EdgeInsets.all(10.0),
            
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children:  [
                Text(title,
                style: const TextStyle(
                  
                  fontSize: 18,
                  color: Colors.white
                  ),
                ),
                SizedBox(height: 5,),

                  Text(body,
                style: const TextStyle(
                  
                  fontSize: 10,
                  color: Colors.white
                  ),
                ),

                ],
            ),
            ),
      ),
    );
  }
}
