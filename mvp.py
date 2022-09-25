import streamlit
from streamlit_agraph import agraph, Node, Edge, Config

nodes = []
edges = []

nodes.append( Node(id="ALI_MOHAMED", 
                   label="ALI_MOHAMED RAGE", 
                   size=25, 
                   color="#ACDBC9",
                   shape="dot"
            ) # includes **kwargs
            )
nodes.append( Node(id="MAALIM_AYMAN", 
                   size=25,
                   color="#ACDBC9",
                   shape="dot") 
            )
nodes.append( Node(id="Al-Shabaab",
                   size = 25,
                   shape="circularImage",
                   image="https://upload.wikimedia.org/wikipedia/en/9/94/ShababLogo.png")
            )
nodes.append( Node(id="Jaysh_Ayman",
                   size = 25,
                   shape="circularImage",
                   image="https://jamestown.org/wp-content/uploads/2018/04/1219492.jpg")
)

edges.append( Edge(source="MAALIM_AYMAN", 
                   label="founder_of", 
                   target="Jaysh_Ayman", 
                   # **kwargs
                   ) 
            ) 

edges.append( Edge(source="ALI_MOHAMED", 
                   label="member_of", 
                   target="Al-Shabaab", 
                   # **kwargs
                   ) 
            ) 

edges.append( Edge(source="Jaysh_Ayman", 
                   label="subgroup_of", 
                   target="Al-Shabaab", 
                   # **kwargs
                   ) 
            )

config = Config(width=500, 
                height=500, 
                # **kwargs
                ) 

return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)