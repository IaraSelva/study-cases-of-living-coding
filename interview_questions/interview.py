class Pipeline:
    def __init__(self, k, packages):
        self.limit = k
        self.packages = packages
        self.queue = []
        self.output = []
        self.check = {}
    
    def check_packages(self):
        while self.packages.hasNext:
            curr = self.packages.next

            if self.exist(curr):
                self.output.append(curr)
            
            if len(self.queue) == self.limit:
                item_to_remove = self.queue.pop(0)
                self.update_items(item_to_remove)
            
            self.queue.append(curr)
            self.update_pipeline(curr)

        return self.output
            
    
    def exist(self, package):
        return package in self.check and self.check[package] > 0
    
    def update_items(self, package):
        self.check[package] -= 1
    
    def update_pipeline(self, package):
        if package not in self.check:
            self.check[package] = 1
        else:
            self.check[package] += 1
