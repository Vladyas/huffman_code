import sys, filecmp

sys.argv.append('-e')
sys.argv.append('wp.txt')

# driver.main()
print(filecmp.cmp('wp.txt', 'wp_e_d.txt', shallow=False))