import networkx as nx
import json
import matplotlib.pyplot as plt


FILENAME = "topics.json"

def space2bl(name):
    for i,c in enumerate(name):
        if c == " ":
            name = name[0:i]+"\n"+name[i+1:]
            break
    return name

if __name__ == "__main__":
    with open(FILENAME,'r') as f:
        json_data = f.read()

#    print(json_data)
    data = json.loads(json_data)
#    print("TOPICS")
#    print(data)

    G = nx.DiGraph()
    remap_dict={}
    color_l = []

    for t in data["topics"]:
        print(t)
        G.add_node(t["id"],name=t["name"])
        remap_dict[t["id"]] = space2bl(t["name"])

        if len(t["requires"]) > 0:
            for i in t["requires"]: 
                G.add_edge(i,t["id"])

        if t["core"]:
            color_l.append(0.7)
        else:
            color_l.append(0.3)

#    print(remap_dict)
    print(sorted(G))
#    nx.relabel_nodes(G,remap_dict)
#    sorted(G)
    pos_d = {1:[0,30], 2:[0,20], 3:[0,0],
             4:[4,35], 5:[1,30], 6:[1,20], 7:[1,0], 8:[1,-5],
             9:[2,30], 10:[3,40], 11:[2,20], 12:[2,15], 13:[2,0], 14:[1,-10],
             15:[3,30], 16:[3,25], 17:[3,15], 18:[3,10], 19:[3,0], 20:[3,-10],
             21:[5,30], 22:[4,30], 23:[4,20], 24:[4,15], 25:[4,5],26:[4,0],
             27:[5,20], 28:[5,10] }
    plt.subplot(111)
#    nx.draw(G, with_labels=True, font_weight='bold')
#    nx.draw_kamada_kawai(G, with_labels=True, labels=remap_dict,pos=pos_d)
    nx.draw(G, with_labels=True, labels=remap_dict,pos=pos_d, node_size=600, font_size=8, node_color=color_l,
            vmin=0, vmax=1, edge_color='blue', label="Cyan: Core Topics. Blue: Optional Topics", font_weight='bold')

    plt.title("Embedded Curriculum\nGreen: Core Topics. Blue: Optional Topics")
    plt.show()

