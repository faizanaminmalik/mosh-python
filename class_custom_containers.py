class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1 # will take care of case sensitivity Python VS python

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags) # This function returns iterator object which gives us one item at a time in for loop

cloud = TagCloud()
cloud.add("python")
cloud.add("python")
cloud.add("Python")
print(cloud.tags)

# To implement the feature of getting result when we specify tag, we implement __getitem__() magic method
print(cloud["python"])

# To implement the feature of getting result when we specify tag, we implement __setitem__() magic method
cloud["python"] = 10
print(cloud["python"])

cloud["java"] = 14
# To implement the feature of len, we implement __len__() magic method
print(len(cloud))

# To implement the feature of iterating in for loo, we implement __iter__() magic method
for tag in cloud:
    print(tag)