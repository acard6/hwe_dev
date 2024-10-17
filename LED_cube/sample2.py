def create_staircase(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets

def create_staircase2(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

def main():
    nums1 = [1,2,3]
    nums2 = [1,2,3,4,5,6,7,8,9]
    C10 = create_staircase(nums1)
    C11 = create_staircase(nums2)
    print(C10,":\t", C11)
    C20 = create_staircase2(nums1)
    C21 = create_staircase2(nums2)
    print(C20,":\t", C21)

if __name__=='__main__':
  main()