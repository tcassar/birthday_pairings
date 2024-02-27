# Birthday Pairings

Pair people together randomly out of some pre-allocated buckets

## Usage

`main.py` accepts a text file. 

```shell
python3 main.py IN
```
will generate a `results.md` where people have been paired together. 

## Format

Input file format is extremely delicate. Don't put newlines at the top of the file. Or end with `---`

Syntax: 
- `---` separates buckets
- `\n` separates a bucket in half s.th. people before the newline can only be matched with people after the newline

## Results for 02/03/2024

See 
    [initial-results.md](https://github.com/tcassar/birthday_pairings/blob/master/initial-results.md) 
    [reallocation #1](https://github.com/tcassar/birthday_pairings/blob/master/results.md) (MOST RECENT)