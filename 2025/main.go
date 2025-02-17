package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"log"
	"os"
)

// ParseGuests parses the guests file.
//
// Format is 1 person per line.
// Ignores lines starting with `#` - purpose is to have partners paired with
// each other where their partner is not at all part of the ecosystem
func ParseGuests(fp string) (map[string]struct{}, error) {
	guests := make(map[string]struct{})

	f, err := os.Open(fp)
	if err != nil {
		return nil, fmt.Errorf("failed to open pairings file: %w", err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)

	for scanner.Scan() {
		person := scanner.Text()
		if err := scanner.Err(); err != nil {
			return nil, fmt.Errorf("failed to read pairings file: %w", err)
		}

		if person == "" {
			break
		}

		if person[0] == byte('#') {
			fmt.Fprintf(os.Stderr, "Skipping %s\n", person[2:])

			continue
		}

		guests[person] = struct{}{}
	}

	return guests, nil
}

func main() {
	guests, err := ParseGuests(os.Args[1])
	if err != nil {
		log.Fatalf("failed to parse guests: %v", err)
	}

	pairs := make(map[string]string)

	var key *string

	// rely on random iteration order of maps for randomising pairs
	for guest := range guests {
		if key == nil {
			key = &guest
		} else {
			pairs[*key] = guest
			key = nil
		}
	}

	if key != nil {
		pairs["Alone"] = *key
	}

	bts, err := json.Marshal(pairs)
	if err != nil {
		log.Fatalf("failed to marshal pairings: %v", err)
	}

	fmt.Println(string(bts))
}
