def merge_ranges(meetings):

    # Merge meeting ranges

    mergedMeetings = []

    sortedMeetings = sorted(meetings)

    mergedMeetings.append(sortedMeetings[0])

    for currentStart, currentEnd in sortedMeetings:
    	lastMergedMeetingStart, lastMergedMeetingEnd = mergedMeetings[len(mergedMeetings) - 1]

    	if lastMergedMeetingEnd >= currentStart:
    		mergedMeetings[len(mergedMeetings) - 1] = (lastMergedMeetingStart, max(lastMergedMeetingEnd, currentEnd))
    	else:
    		mergedMeetings.append((currentStart,currentEnd))
    
    return mergedMeetings

if __name__ == '__main__':
	meetings = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
	# sortedMeetings =  [(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]
	print(merge_ranges(meetings))

