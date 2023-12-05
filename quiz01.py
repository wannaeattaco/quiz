"""Task 1: Streamer Agency

You were hired by Mr. Lamo of the Asterisk Digital Agency (ADA) to implement a screening system for streamer candidates. Asterisk is one of the most well-known streamer and e-sports companies in Thailand with a very strong legal team (100% win rate).

(Note: The story is fictional.)

Implement as much as you can.

First, you must implement a class Candidate based on the following conditions:

The class is named Candidate
The arguments for initialization are as follows:
name: str ... required for init
age: int ... required for init
followers: int ... optional for init, default 0
genre: str ... optional for init, default "unknown"
do NOT implement getters or setters for name, age, followers, or genre
Additionally, the class must have the following properties:
status: str ... set to "new" on init ... has a getter and a setter
Attributes have the following restrictions:
All types above must be enforced, and you must raise TypeError for any violation (including when initializing or when subsequently setting).
For example, trying to set "age" to a float or str must cause TypeError to be raised.
name and genre must not be an empty string or only whitespaces. Raise ValueError if violated.
age and follower must be greater than 0. Raise ValueError if violated.
status must be either "new", "qualified", "accepted", "rejected". Raise ValueError if violated.
Do NOT include any message with exceptions. Just raise.
When printed, a Candidate, for example, named Kenny, age 18, 2000 followers, genre "dog game", status "new", shows up like this:

Candidate: Kenny, 18, 2000, dog game (new)

You may implement as many methods and attributes as you need, but they must be private.
Only the getters and setters may be public."""


class Candidate:
    def __init__(self, name: str, age: int, followers=0, genre="unknown", status="new"):
        if not isinstance((age, followers), int):
            raise TypeError
        if not isinstance((name, genre, status), str):
            raise TypeError
        if name or genre == "" or name or genre == " ":
            raise ValueError
        if age <= 0 or followers <= 0:
            raise ValueError
        status_lst = ["new", "qualified", "accepted", "rejected"]
        if status not in status_lst:
            raise ValueError
        self.__name = name
        self.__age = age
        self.__followers = followers
        self.__genre = genre
        self.__status = status

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status

    def __str__(self):
        return f'Candidate: {self.__name}, {self.__age}, {self.__followers}, {self.__genre} ({self.__status}'


c = Candidate("Kenny", 18, 2000, "dog name", "new")
print(c)
