

import matplotlib.pyplot as plt

def plotqaoa():
    
    highest_energy = 0
    n = 3

    best_guess_mixer_angles = 0
    best_guess_cost_angels = 0

    for i in range(100):
        print(i, end='\r')
        guess_mixer_angles = np.random.uniform(0, 1, n)
        guess_cost_angels = np.random.uniform(0, 1, n)
        variables = np.concatenate((guess_mixer_angles, guess_cost_angels))
        qaoa_energy = qaoa_instance(variables)
        if(qaoa_energy > highest_energy):
            print("new highest energy found: ", end='')        
            print(qaoa_energy)
            best_guess_mixer_angles = guess_mixer_angles
            best_guess_cost_angels = guess_cost_angels
            highest_energy = qaoa_energy

    print("highest_energy: ", end='')
    print(highest_energy)

    print("best_guess_mixer_angles: ", end='')
    print(best_guess_mixer_angles)

    print("best_guess_cost_angels: ", end='')
    print(best_guess_cost_angels)

    for i in range(100):
        print(i, end='\r')
        random1 = np.random.uniform(-1, 1, n)    
        random2 = np.random.uniform(-1, 1, n)

        #random1 = np.random.uniform(-1, 1, n)    
        #random2 = np.random.uniform(-1, 1, n)

        
        # random guess of 1 in 2 * n
        
        p = random.randrange(6)
        guess_mixer_angles = best_guess_mixer_angles
        guess_cost_angels = best_guess_cost_angels
        if(p < 3):
            guess_mixer_angles[p] = max(0.000001, min((best_guess_mixer_angles[p] + random1[p]/np.log(i+2)), 0.999999))
        else:
            p = p - 3
            guess_cost_angels[p] = max(0.000001, min((best_guess_cost_angels[p] + random1[p]/np.log(i+2)), 0.999999))

        # guess_mixer_angles = [max(0.000001, min((param1[j] + random1[j]/np.log(i)), 0.999999))  for j in range(n)]
        # guess_cost_angels = [max(0.000001, min((param2[j] + random2[j]/np.log(i)), 0.999999))  for j in range(n)]
            
        variables = np.concatenate((guess_mixer_angles, guess_cost_angels))
        qaoa_energy = qaoa_instance(variables)
        if(qaoa_energy > highest_energy):
            print("new highest energy found: ", end='')        
            print(qaoa_energy)
            param1 = guess_mixer_angles
            param2 = guess_cost_angels
            highest_energy = qaoa_energy

    print("highest_energy: ", end='')
    print(highest_energy)

    print("best_guess_mixer_angles: ", end='')
    print(best_guess_mixer_angles)

    print("best_guess_cost_angels: ", end='')
    print(best_guess_cost_angels)



def plotresults(results, expectedresults, n=9,a=17 ,b=6):

    def dictionary_sorter(n,given_dict):
        sorted_values=sorted(given_dict.values(), reverse=True)
        sorted_dict={}
        
        for i in sorted_values[:n]:
            for k in given_dict.keys():
                if given_dict[k]==i:
                    sorted_dict[k]=given_dict[k]
                    break
        return sorted_dict
        #returns a dictionary sorted for the top n measurement outcomes

    rank=n #pick a value of n i.e give me the top 10 most counted measurements

    x_vals=list(map(str,dictionary_sorter(rank,results.get_counts()).keys())) #basis states
    y_vals=list(dictionary_sorter(rank,results.get_counts()).values()) #counts

    result_colors = ['red' for i in range(rank)]

    i = 0
    for x in x_vals:
        xtp = x.split('(')[1].split(')')[0].split(',')
        for er in expectedresults:
            distance = 0
            for j in range(len(xtp)):
                if(int(xtp[j]) != er[j]):
                    distance = distance + 1

            if(distance == 0):
                result_colors[i] = 'green'
                    
        i = i + 1

    plt.figure(figsize=(a,b))
    plt.bar(x_vals,y_vals, color=result_colors)
    plt.title("Results")
    plt.xlabel('Basis states')
    plt.ylabel('Counts')

    plt.show()

    # generates a bar chart of basis states vs counts
    # The two equivalent optimal colourings for maxcut will (hopefully) be shown in green
    # with other results shown in red
    # chart expands if rank is changed

    # print("plotresults")
