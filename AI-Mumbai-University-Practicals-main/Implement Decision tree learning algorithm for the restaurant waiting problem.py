import math

class DataSet:
    def __init__(self, ds):
        self.dataset = ds      
    
    def print(self):
        print(self.dataset)
    
    def uniqueAns(self): 
        return len(set(self.dataset["Ans"]))
    
    def getMaxOccur(self):
        d = {self.dataset["Ans"].count(x): x for x in self.dataset["Ans"]}
        keys = sorted(d.keys(), reverse=True)
        return d[keys[0]] if len(keys) > 1 and keys[0] != keys[1] else None
    
    def copy(self):
        newdataset = {key: self.dataset[key].copy() for key in self.dataset.keys()}
        return DataSet(newdataset)

    def maxInfoGain(self):
        features = self.dataset["Features"]
        if features:
            maxinfogain = self.infoGain(features[0])
            maxfeat = features[0]
            for feat in features:
                ig = self.infoGain(feat)                
                if ig >= maxinfogain:
                    maxinfogain = ig
                    maxfeat = feat
            return maxfeat
        return None
            
    def infoGain(self, feat):
        if feat in self.dataset:
            featlist1 = self.dataset[feat]
            total = len(featlist1)
            featset = set(featlist1)
            d = {item: featlist1.count(item) for item in featset}
            branches = self.splitOnFeature(feat)
            gain = sum((d[key] / total) * dsobj.getEntropy() for key, dsobj in branches.items())
            return self.getEntropy() - gain
        print("Feature does not exist")
        return None

    def getEntropy(self):
        list1 = self.dataset["Ans"]
        total = len(list1)
        aset = set(list1)
        d = {item: list1.count(item) for item in aset}
        ent = -sum((d[k]/total) * math.log(d[k]/total, 2) for k in aset)
        return ent
        
    def splitOnFeature(self, feat):
        if feat in self.dataset["Features"]:
            ans_set = set(self.dataset[feat])
            newfeatures = self.dataset["Features"].copy()
            newfeatures.remove(feat)
            newdataset = {akey: [] for akey in self.dataset.keys() if akey != feat}
            newdataset["Features"] = newfeatures
            branches = {akey: {key: [] for key in newdataset} for akey in ans_set}
            
            for i, featval in enumerate(self.dataset[feat]):
                if featval in branches:
                    branches[featval]["Ans"].append(self.dataset["Ans"][i])
                    for nfeat in newfeatures:
                        branches[featval][nfeat].append(self.dataset[nfeat][i])
            
            for key in branches:
                branches[key] = DataSet(branches[key])
                
            return branches
        print(feat, "feature is not available")
        return None

def calculateAns(dsobj, feature, maxoccur, descr):
    branches = dsobj.splitOnFeature(feature)
    
    for key, newdsobj in branches.items():
        if newdsobj.uniqueAns() == 1:
            print("Answer for", descr + "-" + feature, "with value =", key, "is:", newdsobj.dataset['Ans'][0])
        elif newdsobj.uniqueAns() == 0 or (newdsobj.uniqueAns() > 1 and not newdsobj.dataset["Features"]):
            print("Answer for", descr + "-" + feature, "with value =", key, "is:", maxoccur)            
        else:
            newfeat = newdsobj.maxInfoGain()
            newmaxoccur = newdsobj.getMaxOccur() or maxoccur
            calculateAns(newdsobj, newfeat, newmaxoccur, descr + ":" + feature + ":->" + key + " ")

dataset = {
    "Ans": ["Wait", "Wait", "Leave", "Wait", "Wait", "Wait", "Leave", "Leave", "Wait", "Leave"],
    "Features": ["Reservation", "Raining", "BadService"],
    "Reservation": ["T", "T", "T", "F", "T", "T", "T", "T", "T", "F"],
    "Raining": ["T", "F", "T", "T", "T", "T", "F", "T", "T", "F"],
    "BadService": ["F", "F", "T", "F", "F", "F", "T", "T", "F", "F"]
}

d1 = DataSet(dataset)
if d1.uniqueAns() != 1:
    feat = d1.maxInfoGain()
    calculateAns(d1, feat, d1.getMaxOccur(), "")
