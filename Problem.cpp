#include <bits/stdc++.h>
using namespace std;
int main (){

    string books[20] = {
        "The Great Gatsby",
        "To Kill a Mockingbird",
        "1984",
        "Pride and Prejudice",
        "The Catcher in the Rye",
        "The Hobbit",
        "Fahrenheit 451",
        "One Hundred Years of Solitude",
        "The Lord of the Rings",
        "Brave New World",
        "The Grapes of Wrath",
        "Moby-Dick",
        "The Odyssey",
        "Crime and Punishment",
        "The Scarlet Letter",
        "Wuthering Heights",
        "Frankenstein",
        "Dracula",
        "Alice's Adventures in Wonderland",
        "War and Peace"
    };




    int count=20;

    cout<<"The total book list are: "<<endl;
    for(int i=0;i<20;i++){
        cout<<books[i]<<endl;
    }


    cout<<endl;

    cout<<"Do you want to borrow or return the book"<<endl;
    cout<<"If u want to borrow then press 1 or if you want to return press 0"<<endl;
    int a;
    cin>>a;
    if(a==1){
        cout<<"How many books you want to borrow?"<<endl;
        int c;
        cin>>c;
        if(count-c<0){
            cout<<"There is insufficient books for borrowing"<<endl;
        }
        else
        cout<<"The total number of book after borrowing: "<<count-c<<endl;
    }
    else {
         cout<<"How many books you want to return?"<<endl;
        int c;
        cin>>c;
        if(count+c>20)
        cout<<"No books are borrowed"<<endl;
        else 
        cout<<"The total number of book after returning: "<<count+c<<endl;
    }





    return 0;
}