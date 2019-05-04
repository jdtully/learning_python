#Find smallest number is divisible by all the items in the list.
def find_lcm_for_range(r):
   # list_of_factors=get_factorisations_for_range(r)
    lcm_factors=dict()   
    for k in list_of_factors.keys():
        #getfactorization  for K
        current_factors=list_of_factors[k]
        counts=count_items_in_list(current_factors)
        for ck in counts.keys():
            if ck in lcm_factors:
                if lcm_factors[ck]<counts[ck]:
                    lcm_factors[ck] = counts[ck]
            else:
                lcm_factors[ck]=counts[ck]  

        return lcm_factors

get_factorization = [2, 2, 5]
factors_list={2: [2], 3: [3], 4: [2, 2], 5: [5], 6: [2, 3], 7: [7], 8: [2, 2, 2], 9: [3, 3], 10: [2, 5], 11: [11], 12: [2, 2, 3], 13: [13], 14: [2, 7], 15: [3, 5], 16: [2, 2, 2, 2], 17: [17], 18: [2, 3, 3], 19: [19], 20: [2, 2, 5]}
print(find_lcm_for_range(factors_list))