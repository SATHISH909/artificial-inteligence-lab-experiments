import math

# Calculate entropy of a dataset
def entropy(data):
    labels = [row[-1] for row in data]
    unique_labels = set(labels)
    entropy_value = 0
    for label in unique_labels:
        prob = labels.count(label) / len(labels)
        entropy_value -= prob * math.log2(prob)
    return entropy_value

# Split dataset based on attribute
def split_data(data, column, value):
    subset = [row for row in data if row[column] == value]
    return subset

# Choose best feature to split on (using Information Gain)
def best_feature_to_split(data):
    base_entropy = entropy(data)
    num_features = len(data[0]) - 1
    best_info_gain = 0
    best_feature = -1

    for i in range(num_features):
        values = set(row[i] for row in data)
        new_entropy = 0
        for value in values:
            subset = split_data(data, i, value)
            prob = len(subset) / len(data)
            new_entropy += prob * entropy(subset)
        info_gain = base_entropy - new_entropy
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature = i
    return best_feature

# Build Decision Tree recursively
def build_tree(data, features):
    labels = [row[-1] for row in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if len(data[0]) == 1:
        return max(set(labels), key=labels.count)

    best_feat = best_feature_to_split(data)
    best_feat_name = features[best_feat]
    tree = {best_feat_name: {}}

    values = set(row[best_feat] for row in data)
    for value in values:
        sub_features = features[:best_feat] + features[best_feat+1:]
        subset = split_data(data, best_feat, value)
        sub_data = [row[:best_feat] + row[best_feat+1:] for row in subset]
        tree[best_feat_name][value] = build_tree(sub_data, sub_features)

    return tree

# Example dataset
dataset = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
]

features = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# Build the decision tree
tree = build_tree(dataset, features)
print("🌳 Decision Tree (ID3):")
print(tree)
