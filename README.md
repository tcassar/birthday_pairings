# Pubcrawl Pairings

## How this works

- You get randomly paired a partner
- You turn up dressed in costume with your partner
- The 2025 theme: **things that go well together**

- For example
    - Salt and Vinegar
    - Ketchup and Mustard
    - 256 and disappointment

## Pairing Results

### Initial Pairings
These are _subject to change_ if people cannot make it. If your partner can make it, then these pairings are **fixed**.

```json
{
    "Alex Bush": "John Heereboys",
    "Anna Bray": "Tom Cassar",
    "Bea Page": "Ivan Ly",
    "Ben Cullen": "Jasmine Eid",
    "Charlie Larrier": "Mr Charlie Larrier",
    "Cyrus Knopf": "Lourenco Silva",
    "Dhruv Patel": "Erin Balls",
    "Ed Cassar": "Laurie Megainey",
    "Finn Burns": "Dennis Gendis",
    "Flower Graham": "Tilly Kendall",
    "Fran Bedford": "Marcus Charlesworth",
    "Frisbee Choi": "Daisy Steen",
    "Grace Robertson": "Kai Steele",
    "Hannah Abbot": "Emily Somner",
    "Hariett Clover": "Maisy Munroe",
    "Henry Myall": "Claudine",
    "Ioan Gwenter": "Keira Strauss",
    "Jacob Blunt": "Tom Jenkins",
    "Jamila Grau": "Elise Humpreys",
    "Jay Barnett": "Will Swanton",
    "Jess Osborn": "Callum McAnearny",
    "Josh Tupaz": "Joel Arulpragasam",
    "Kallina Paul": "Brad Bell",
    "Kezzy Boy": "Brainna Neagu",
    "Khushi Jain": "Anshul Prushty",
    "Kian Mazloum": "Phoebe Summer",
    "Lewis Wild": "Mathilde Mesquito de Melo",
    "Louis Edmondson": "Abbie Walton",
    "Lukey 🅱️ ": "Alex Redford",
    "Marianne Garcia": "Kamran Howard",
    "Miles Groizard": "Olly RG",
    "Montgomenry": "Eray Baykal",
    "Oscar Ross": "Dev Soneji",
    "Owen Michaels": "Marco Ferrucci",
    "Patrick Mermelstien-Lyons": "Chris Murray",
    "Romy Kershaw": "Emily Clarkson",
    "Ryan Hughes": "Reuben Briggs",
    "Sai Putravu": "Jakup Rozanski",
    "Spencer Abson": "Matt Conroy",
    "Topsy Perrington": "Mr. Topsy Perrington",
    "Xander Hudson": "Alex Havelin"
}
```

## Don't believe its random?

How dare you question my integrity!

Source code publihed in [2025/main.go](https://github.com/tcassar/birthday_pairings/blob/master/2025/main.go) (yes, its `go` this year :))


If you have `go` installed, clone the repo, `cd 2025`, 

```shell
go run main.go ./people.txt  | jq
```

for pretty printed output with jq

