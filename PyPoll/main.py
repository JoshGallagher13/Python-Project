import os
import csv

csvpath = os.path.join('Resources','election_data.csv')


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    
    vote_count = 0
    votes=[]
    tally=[]
    perc=[]
    winner=0
    for row in csvreader:
        vote_count+=1
        votes.append(row[2])
    canidates=list(set(votes))
    for canidate in range(len(canidates)):
        tally.append(int(votes.count(canidates[canidate])))
        perc.append((int(((tally[canidate]/vote_count)*100))))
        winner=canidates[perc.index(max(perc))]
    zipped=list(zip(tally,perc,canidates))
    zipped.sort(reverse=True)
    print(f'Election Results \n----------\nTotal Votes: {vote_count}\n----------')
    for i in range(len(zipped)):
        print(f'{zipped[i][2]} {zipped[i][1]}% ({zipped[i][0]})')
    print(f'----------\nWinner: {winner}\n----------')

    output_path = os.path.join("Analysis", "Analysis.txt")
   
    with open(output_path, 'w', newline='') as newfile:
        newfile.write(f'Election Results \n----------\nTotal Votes: {vote_count}\n----------\n')
        for i in range(len(zipped)):
            newfile.write(f'{zipped[i][2]} {zipped[i][1]}% ({zipped[i][0]})\n')
        newfile.write(f'----------\nWinner: {winner}\n----------')