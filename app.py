import streamlit as st, pandas as pd, numpy as np, plotly.express as px
st.title("Supply Chain Analytics"); st.caption("Synthetic SKU inventory and replenishment planning.")
r=np.random.default_rng(31); n=350
d=pd.DataFrame({"sku":[f"SKU-{i:04}" for i in range(n)],"category":r.choice(["Electronics","Home","Apparel","Grocery"],n),"on_hand":r.integers(0,900,n),"daily_demand":r.uniform(1,35,n),"lead_time":r.integers(2,35,n),"unit_cost":r.uniform(4,250,n)})
d["reorder_point"]=d.daily_demand*d.lead_time+1.65*np.sqrt(d.daily_demand*d.lead_time); d["inventory_value"]=d.on_hand*d.unit_cost
d["status"]=np.where(d.on_hand<d.reorder_point,"Reorder",np.where(d.on_hand>3*d.reorder_point,"Overstock","Healthy"))
cats=st.multiselect("Category",d.category.unique(),default=list(d.category.unique())); v=d[d.category.isin(cats)].copy()
a,b,c=st.columns(3); a.metric("SKUs",len(v)); b.metric("Inventory value",f"${v.inventory_value.sum():,.0f}"); c.metric("Reorder alerts",int((v.status=="Reorder").sum()))
st.plotly_chart(px.pie(v,names="status"),use_container_width=True); st.plotly_chart(px.scatter(v,x="daily_demand",y="on_hand",color="status",hover_name="sku"),use_container_width=True)
v["suggested_order_qty"]=(2*v.reorder_point-v.on_hand).clip(lower=0).round().astype(int); st.dataframe(v.sort_values("suggested_order_qty",ascending=False).head(50))
st.download_button("Export replenishment plan",v.to_csv(index=False),"replenishment.csv")
