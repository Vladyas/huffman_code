import pickle
# t = dict()
# with open('wp.txt', 'r', encoding='iso-8859-1') as f:
#     a = f.read(100)
#     for i in a:
#         t[i] = 1
#         pass

a = {1:1, 2:2, 3:3}
with open('test_pickle.txt', 'wb') as f:
    pickle.dump(a, f)
with open('test_pickle_dumps.txt', 'wb') as f:
    f.write(pickle.dumps(a))
