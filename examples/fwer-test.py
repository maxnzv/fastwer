#!/usr/bin/env python3

import fastwer

# hypo = ['This is an example .', 'This is another example .']
# ref = ['This is the example :)', 'That is the example .']

hypo = ["Knot only are the Springs Preserve",
	"important locally and within the state",
	"of Nevada by being placed on the",
	"National Register of Historic Places.",
	"It is significant to the history, the",
	"national history of the United States.",
	"And our archaeologists are always",
	"observing the surface features of any",
	"potentially historic site for clues",
	"about what might lie below...",
	"waiting two bee uncovered.",
	"Well before I came on us",
	"archaeologists there was evidence of the",
	"sort off the ground subside in the ground",
	"sinking in in an area and the",
	"archaeological staff at the time went to",
	"go investigate that thinking perhaps",
	"that it was a collapsed pipe. So they",
	"went in with some back Owen and removed",
	"some of the overburden and found",
	"evidence of some of the metalic band that",
	"would wrap around those redwood pipe.",
	"So we new were was located and so we",
	"decided with the construction of",
	"boom town that we might want to have some",
	"more examples of that redwood pipe.",
	"Over the past several months we've been",
	"out there excavating uncovering that.",
	"What's thrilling about this find us",
	"museum class story that",
	"deserves showing and telling."]

ref = ["Not only is the Springs Preserve",
	"important locally and within the state",
	"of Nevada by being placed on the",
	"National Register of Historic Places.",
	"It is significant to the history, the",
	"national history of the United States.",
	"And our archaeologists are always",
	"observing the surface features of any",
	"potentially historic site for clues",
	"about what might lie below...",
	"waiting to be uncovered.",
	"Well before I came on as",
	"archaeologists there was evidence of the",
	"sort of the ground subside in the ground",
	"sinking in in an area and the",
	"archaeological staff at the time went to",
	"go investigate that thinking perhaps",
	"that it was a collapsed pipe. So they",
	"went in with some back Owen and removed",
	"some of the overburden and found",
	"evidence of some of the metal bands that",
	"would wrap around those redwood pipe.",
	"So we knew where was located and so we",
	"decided with the construction of",
	"boomtown that we might want to have some",
	"more examples of that redwood pipe.",
	"Over the past several months we've been",
	"out there excavating uncovering that.",
	"What's thrilling about this find is a",
	"museum class story that",
	"deserves showing and telling."]

print ("Corpus-Level WER: 7.2917", fastwer.score(hypo, ref))
print ("Corpus-Level CER: 1.6729", fastwer.score(hypo, ref, char_level=True))

print ("Sentence-Level WER: 33.3333", fastwer.score_sent(hypo[0], ref[0]))
print ("Sentence-Level CER: 15.625", fastwer.score_sent(hypo[0], ref[0], char_level=True))