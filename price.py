def get_summ (one, two, delimiter='&'):
    get_summ_count = one+delimiter+two
    print(get_summ_count)
    return get_summ_count


# one='kk'
# two='tyuu'
# delimeter='&'
# get_summ_count = one+delimiter+two
# print(get_summ_count)
# one2= get_summ_count

one2=get_summ('kk', 'tyuu')
print(one2)


start=get_summ('learn', 'python').upper()
print (start)

