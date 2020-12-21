## API
- The list of 401n2 students is hard-coded on lines 50-71. Absent students can be commented out and will not be included into the final groups;
- Default group size is 2. To edit the size of each group, the new number can be passed to the `get_random_pairs` function (line 74) as a second parameter.
- If there's remainder after dividing the students into groups - all extra students will be added to the last group;
- After running the script the final groups will be outputted to the console as a string.