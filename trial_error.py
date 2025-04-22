# # # streamlit_app.py

# # import streamlit as st

# # st.set_page_config(page_title="FootingPro - Pad Footing Design", layout="centered")

# # st.title("🧱 Isolated Pad Footing Design Tool")

# # st.markdown("""
# # This tool helps you design an isolated pad footing based on applied loads, soil capacity, and material strengths.
# # """)

# # with st.form("input_form"):
# #     st.subheader("🔧 Input Parameters")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         dead_load = st.number_input("Dead Load (kN)", min_value=0.0, value=950.0)
# #         fcu = st.number_input("Concrete Strength fcu (N/mm²)", min_value=0.0, value=35.0)
# #         column_width = st.number_input("Column Width (mm)", min_value=0.0, value=300.0)
# #     with col2:
# #         live_load = st.number_input("Live Load (kN)", min_value=0.0, value=200.0)
# #         fy = st.number_input("Steel Yield Strength fy (N/mm²)", min_value=0.0, value=500.0)
# #         soil_bearing_capacity = st.number_input("Safe Bearing Capacity (kN/m²)", min_value=0.0, value=170.0)

# #     submitted = st.form_submit_button("Calculate Footing")

# # if submitted:
# #     # Ultimate load (assuming partial safety factors)
# #     factored_load = 1.35 * dead_load + 1.5 * live_load

# #     # Required footing area
# #     required_area = factored_load / soil_bearing_capacity

# #     # Assume square footing
# #     footing_size = required_area ** 0.5
# #     footing_size = round(footing_size, 2)
# #     qu = factored_load/footing_size
# #     ultimate_pressure = qu
# #     st.success("✅ Design Results")
# #     st.write(f"**Factored Load:** {factored_load:.2f} kN")
# #     st.write(f"**Ultimate Pressure:** {ultimate_pressure:.2f} kN/m²")
# #     st.write(f"**Required Footing Area:** {required_area:.2f} m²")
# #     st.write(f"**Footing Size (Square):** {footing_size:.2f} m x {footing_size:.2f} m")

# #     st.info("Reinforcement and detailing to be added in next version.")

# # streamlit_app.py

# # import streamlit as st
# # import math

# # st.set_page_config(page_title="FootingPro - Pad Footing Design", layout="wide")

# # st.title("🧱 FootingPro: Pad Footing Design Tool")

# # st.markdown("""
# # This tool assists professionals and students in designing an **Isolated Pad Footing** based on applied loads, soil conditions, and material strengths.
# # Compatible with desktop and mobile devices.
# # """)

# # with st.form("input_form"):
# #     st.subheader("🔧 Input Parameters")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         dead_load = st.number_input("Dead Load (kN)", min_value=0.0, value=950.0)
# #         fcu = st.number_input("Concrete Strength fcu (N/mm²)", min_value=0.0, value=35.0)
# #         column_width = st.number_input("Column Width (mm)", min_value=0.0, value=300.0)
# #     with col2:
# #         live_load = st.number_input("Live Load (kN)", min_value=0.0, value=200.0)
# #         fy = st.number_input("Steel Yield Strength fy (N/mm²)", min_value=0.0, value=500.0)
# #         soil_bearing_capacity = st.number_input("Safe Bearing Capacity (kN/m²)", min_value=0.0, value=170.0)

# #     submitted = st.form_submit_button("🔍 Calculate Footing")

# # if submitted:
# #     st.subheader("📊 Design Summary")

# #     # Ultimate load (assuming partial safety factors)
# #     factored_load = 1.35 * dead_load + 1.5 * live_load

# #     # Required footing area
# #     required_area = factored_load / soil_bearing_capacity

# #     # Assume square footing
# #     footing_size = round(required_area ** 0.5, 2)  # meters

# #     # Ultimate bearing pressure
# #     ultimate_pressure = round(factored_load / (footing_size ** 2), 2)

# #     st.success("✅ Design Results")
# #     st.markdown(f"**Factored Load:** {factored_load:.2f} kN")
# #     st.markdown(f"**Ultimate Pressure:** {ultimate_pressure:.2f} kN/m²")
# #     st.markdown(f"**Required Footing Area:** {required_area:.2f} m²")
# #     st.markdown(f"**Footing Size (Square):** {footing_size:.2f} m × {footing_size:.2f} m")

# #     st.divider()
# #     st.subheader("🧮 Reinforcement Calculation (Simplified)")

# #     cover = 50  # mm assumed cover
# #     d = column_width - 2 * cover  # effective depth in mm
# #     moment = (factored_load * 1000) * (footing_size / 2)  # approximate moment in kNm
# #     lever_arm = 0.9 * d / 1000  # in meters
# #     Ast = moment * 1e6 / (0.95 * fy * lever_arm * 1e6)  # in m², then mm²
# #     Ast = round(Ast * 1e6, 2)  # mm²

# #     st.markdown(f"**Effective Depth (d):** {d:.2f} mm")
# #     st.markdown(f"**Approx. Ultimate Moment:** {moment:.2f} kNm")
# #     st.markdown(f"**Required Area of Steel (Ast):** {Ast:.2f} mm²")

# #     st.warning("📌 Use professional judgment and local codes to refine reinforcement layout.")

#     # st.divider()
#     # st.caption("Designed with ❤️ for Civil Engineers and Students.")

# # streamlit_app.py

# # import streamlit as st

# # st.set_page_config(page_title="FootingCalc Pro", layout="wide")

# # # ───────────────────────────────────────────────────────────────
# # # HEADER SECTION (App Name & Tagline)
# # # ───────────────────────────────────────────────────────────────
# # st.markdown("""
# #     <div style='text-align: left; font-size: 28px; font-weight: bold;'>FootingCalc Pro</div>
# #     <div style='text-align: right; font-size: 16px;'>Design Civil Footings with Confidence</div>
# #     <hr style='margin-top: 0.5rem; margin-bottom: 1rem;'>
# # """, unsafe_allow_html=True)

# # # ───────────────────────────────────────────────────────────────
# # # HERO SECTION - Start Designing Button
# # # ───────────────────────────────────────────────────────────────
# # st.markdown("""
# #     <div style='text-align: center;'>
# #         <h1 style='margin-bottom: 1rem;'>Start Designing</h1>
# #     </div>
# # """, unsafe_allow_html=True)

# # # ───────────────────────────────────────────────────────────────
# # # INPUT FORM SECTION
# # # ───────────────────────────────────────────────────────────────
# # with st.form("input_form"):
# #     st.subheader("🔧 Input Parameters")

# #     col1, col2 = st.columns(2)
# #     with col1:
# #         dead_load = st.number_input("Dead Load (kN)", min_value=0.0, value=950.0)
# #         fcu = st.number_input("Concrete Strength fcu (N/mm²)", min_value=0.0, value=35.0)
# #         column_width = st.number_input("Column Width (mm)", min_value=0.0, value=300.0)
# #     with col2:
# #         live_load = st.number_input("Live Load (kN)", min_value=0.0, value=200.0)
# #         fy = st.number_input("Steel Yield Strength fy (N/mm²)", min_value=0.0, value=500.0)
# #         soil_bearing_capacity = st.number_input("Safe Bearing Capacity (kN/m²)", min_value=0.0, value=170.0)

# #     submitted = st.form_submit_button("Calculate Footing")

# # # ───────────────────────────────────────────────────────────────
# # # DESIGN RESULTS
# # # ───────────────────────────────────────────────────────────────
# # if submitted:
# #     factored_load = 1.35 * dead_load + 1.5 * live_load
# #     required_area = factored_load / soil_bearing_capacity
# #     footing_size = round(required_area ** 0.5, 2)
# #     qu = factored_load / footing_size
# #     ultimate_pressure = qu

# #     st.markdown("## ✅ Design Results")
# #     st.write(f"**Factored Load:** {factored_load:.2f} kN")
# #     st.write(f"**Ultimate Pressure:** {ultimate_pressure:.2f} kN/m²")
# #     st.write(f"**Required Footing Area:** {required_area:.2f} m²")
# #     st.write(f"**Footing Size (Square):** {footing_size:.2f} m x {footing_size:.2f} m")

# # # ───────────────────────────────────────────────────────────────
# # # APP OVERVIEW SECTION
# # # ───────────────────────────────────────────────────────────────
# # st.markdown("---")
# # st.markdown("## 📘 App Overview")
# # st.markdown("""
# # This app allows you to design isolated pad footings based on safe bearing capacity, load values, and material strengths — all in one click.
# # """)

# # # ───────────────────────────────────────────────────────────────
# # # BENEFIT PANELS SECTION
# # # ───────────────────────────────────────────────────────────────
# # st.markdown("---")
# # st.markdown("## 🌟 Benefits")

# # col1, col2, col3, col4 = st.columns(4)
# # with col1:
# #     st.image("https://img.icons8.com/ios/100/000000/ok--v1.png", width=60)
# #     st.caption("**Easy Design**")
# # with col2:
# #     st.image("https://img.icons8.com/ios/100/000000/document--v1.png", width=60)
# #     st.caption("**Auto-report**")
# # with col3:
# #     st.image("https://img.icons8.com/ios/100/000000/line-chart--v1.png", width=60)
# #     st.caption("**Visual Diagrams**")
# # with col4:
# #     st.image("https://img.icons8.com/ios/100/000000/graduation-cap--v1.png", width=60)
# #     st.caption("**Educational**")

# # # ───────────────────────────────────────────────────────────────
# # # FOOTER SECTION
# # # ───────────────────────────────────────────────────────────────
# # st.markdown("---")
# # col1, col2, col3, col4 = st.columns(4)
# # col1.markdown("[Contact](mailto:you@example.com)")
# # col2.markdown("[LinkedIn](https://www.linkedin.com)")
# # col3.markdown("[Disclaimer](#)")
# # col4.markdown("**Version 1.0**")

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np

# # Page configuration
# st.set_page_config(page_title="Square Pad Footing Design", layout="wide")

# # Tabs setup
# tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View"])

# # ----------------------------
# # 1. Project Overview Tab
# # ----------------------------
# with tabs[0]:
#     st.title("Square Pad Footing Design")
#     st.markdown("""
#     This application performs the structural design of a square pad footing
#     supporting a centrally loaded square column based on Eurocode 2 provisions.
    
#     Enter your input parameters in the sidebar to get started.
#     """)

#     with st.sidebar:
#         st.header("Input Parameters")
#         col_size = st.number_input("Column Size (mm)", value=300)
#         dead_load = st.number_input("Dead Load (kN)", value=950.0)
#         imposed_load = st.number_input("Imposed Load (kN)", value=200.0)
#         fcu = st.number_input("Concrete Strength fcu (N/mm²)", value=35.0)
#         fy = st.number_input("Steel Yield Strength fy (N/mm²)", value=500.0)
#         safe_bearing = st.number_input("Safe Bearing Capacity (kN/m²)", value=170.0)

#     total_load = dead_load + imposed_load
#     factored_load = 1.35 * dead_load + 1.5 * imposed_load

#     st.write("### Summary of Inputs")
#     st.write(f"Column size: {col_size} mm")
#     st.write(f"Total service load: {total_load:.2f} kN")
#     st.write(f"Factored load: {factored_load:.2f} kN")
#     st.write(f"Safe bearing capacity: {safe_bearing:.1f} kN/m²")

# # ----------------------------
# # 2. Punching Shear Check Tab
# # ----------------------------
# with tabs[1]:
#     st.header("Punching Shear Check")
#     footing_area = 1.1 * factored_load / 1.4 * safe_bearing  # in m²
#     footing_side = np.sqrt(footing_area)  # m
#     footing_side_mm = footing_side * 1000

#     import math
#     d = 150
#     effective_depth = 340 # mm
#     d_m = effective_depth/1000
#     critical_perimeter = 2 * (col_size + col_size) + (4 * math.pi * d)
#     Pcr = critical_perimeter
#     critical_area = (col_size + (4 * d_m)) * (col_size + (4 * d_m)) - ((4 - math.pi) * 2.0 * (d_m ** 2))
#     Acr = critical_area
#     column_side = col_size
#     perimeter = 4 * (col_size + 2 * 1.5 * 150)  # d = 150 mm assumed
#     V = factored_load * 1e3  # Convert to N
    
#     b0 = 4 * (col_size + d)
#     v_ed = V / (b0 * d)
#     v_rd_c = 0.5 * (fcu ** 0.5)

    
#     net_upward_pressure = factored_load / (footing_side ** 2)
#     V_net_kN = net_upward_pressure * (footing_side ** 2 - Acr)  # kN
#     V_net_N = V_net_kN * 1e3  # Convert to N
#     Vpunch = V_net_N / (Pcr * effective_depth)  # N/mm²

#     st.write(f"Footing size (approx): {footing_side_mm:.0f} mm × {footing_side_mm:.0f} mm")
#     st.write(f"Critical Perimeter (Pcr): {round(Pcr, 2)} mm")
#     st.write(f"Area within critical perimeter (Acr): {round(Acr, 4)} m²")
#     st.write(f"Punching shear stress: {v_ed:.2f} N/mm²")
#     st.write(f"Punching shear capacity: {v_rd_c:.2f} N/mm²")
#     st.write(f"Punching Shear Stress: {Vpunch:.3f} N/mm²")
    
#     if v_ed < v_rd_c:
#         st.success("Punching shear check PASSED.")
#     else:
#         st.error("Punching shear check FAILED.")

# # ----------------------------
# # 3. Moment & Reinforcement Tab
# # ----------------------------
# with tabs[2]:
#     st.header("Moment and Reinforcement Design")
#     net_upward_pressure = factored_load / (footing_side ** 2)
#     lever_arm = footing_side / 2 - (col_size / 1000 / 2)
#     M = net_upward_pressure * lever_arm ** 2 / 2
#     M_kNm = M

#     st.write(f"Factored moment (Mx = My): {M_kNm:.2f} kNm")

#     z = 0.95 * d  # lever arm
#     M_Nmm = M_kNm * 1e6
#     As = M_Nmm / (0.95 * 500 * z)
#     st.write(f"Required reinforcement area (As): {As:.2f} mm²")

#     # Reinforcement Suggestion (12 mm bars)
#     bar_dia = 12
#     area_single_bar = np.pi * (bar_dia / 2) ** 2
#     spacing = (1000 * area_single_bar) / As
#     st.write(f"Provide T12 bars @ {spacing:.0f} mm c/c in both directions")

# # ----------------------------
# # 4. 2D Plan View Tab
# # ----------------------------
# with tabs[3]:
#     st.header("2D Plan View")
#     fig = go.Figure()

#     # Footing outline
#     fig.add_shape(type="rect", x0=0, y0=0, x1=footing_side_mm, y1=footing_side_mm,
#                   line=dict(color="black", width=3), name="Footing")

#     # Column outline
#     center = footing_side_mm / 2
#     col_half = col_size / 2
#     fig.add_shape(type="rect", x0=center - col_half, y0=center - col_half,
#                   x1=center + col_half, y1=center + col_half,
#                   line=dict(color="blue", width=3), name="Column")

#     fig.update_layout(title="2D Plan View of Footing & Column", width=600, height=600,
#                       xaxis=dict(visible=False), yaxis=dict(visible=False), showlegend=False)
#     st.plotly_chart(fig)

# # ----------------------------
# # 5. 3D Reinforcement View Tab
# # ----------------------------
# with tabs[4]:
#     st.header("3D Reinforcement View")
#     bar_positions_x = np.arange(50, footing_side_mm, spacing)
#     bar_positions_y = np.arange(50, footing_side_mm, spacing)

#     fig3d = go.Figure()

#     for x in bar_positions_x:
#         fig3d.add_trace(go.Scatter3d(x=[x, x], y=[0, footing_side_mm], z=[0, 0],
#                                      mode='lines', line=dict(color='red', width=5), name='Bar X'))

#     for y in bar_positions_y:
#         fig3d.add_trace(go.Scatter3d(x=[0, footing_side_mm], y=[y, y], z=[-10, -10],
#                                      mode='lines', line=dict(color='green', width=5), name='Bar Y'))

#     # Column block
#     fig3d.add_trace(go.Mesh3d(
#         x=[center - col_half, center + col_half, center + col_half, center - col_half,
#            center - col_half, center + col_half, center + col_half, center - col_half],
#         y=[center - col_half, center - col_half, center + col_half, center + col_half,
#            center - col_half, center - col_half, center + col_half, center + col_half],
#         z=[0, 0, 0, 0, 300, 300, 300, 300],
#         color='blue', opacity=0.5, name='Column', showscale=False
#     ))

#     fig3d.update_layout(title="3D Reinforcement View", scene=dict(
#         xaxis=dict(title='X'), yaxis=dict(title='Y'), zaxis=dict(title='Z'),
#         aspectratio=dict(x=1, y=1, z=0.3)
#     ))

#     st.plotly_chart(fig3d, use_container_width=True)
####################################### above modified

##################################################################################################

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np
# import math

# # Page configuration
# st.set_page_config(page_title="Square Pad Footing Design", layout="wide")


# st.write("Welcome to the design tool page.")

# if st.button("Go to Home"):
#     st.switch_page("landing_page.py")  # Or whatever your main page file is named

# # Tabs setup
# tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View"])

# # ----------------------------
# # 1. Project Overview Tab
# # ----------------------------
# with tabs[0]:
#     st.title("Square Pad Footing Design")
#     st.markdown("""
#     This application performs the structural design of a square pad footing
#     supporting a centrally loaded square column based on Eurocode 2 provisions.

#     Enter your input parameters in the sidebar to get started.
#     """)

#     with st.sidebar:
#         st.header("Input Parameters")
#         # col_size = st.number_input("Column Size (mm)", value=300)
#         dead_load = st.number_input("Dead Load (kN)", value=950.0)
#         imposed_load = st.number_input("Imposed Load (kN)", value=200.0)
#         fcu = st.number_input("Concrete Strength fcu (N/mm²)", value=35.0)
#         fy = st.number_input("Steel Yield Strength fy (N/mm²)", value=500.0)
#         safe_bearing = st.number_input("Safe Bearing Capacity (kN/m²)", value=170.0)

#     total_load = dead_load + imposed_load
#     factored_load = 1.35 * dead_load + 1.5 * imposed_load

#     # Calculate initial footing size based on factored load and bearing capacity
#     footing_area_calculated = 1.1 * factored_load / (1.4 * safe_bearing)  # in m²
#     footing_side_calculated = np.sqrt(footing_area_calculated)  # m
#     footing_side_mm_calculated = footing_side_calculated * 1000

#     st.write("### Summary of Inputs")
#     # st.write(f"Column size: {col_size} mm")
#     st.write(f"Total service load: {total_load:.2f} kN")
#     st.write(f"Factored load: {factored_load:.2f} kN")
#     st.write(f"Safe bearing capacity: {safe_bearing:.1f} kN/m²")
#     st.write(f"Calculated Footing Size (approx): {footing_side_mm_calculated:.0f} mm × {footing_side_mm_calculated:.0f} mm")

# # ----------------------------
# # 2. Punching Shear Check Tab
# # ----------------------------
# with tabs[1]:
#     st.header("Punching Shear Check")

#     provided_footing_side_mm = st.number_input("Provided Footing Side Length (mm)", value=int(footing_side_mm_calculated), help="Use the actual side length you will provide.")
#     footing_depth = st.number_input("Footing Depth (h) for Base (mm)", value=400, min_value=150)
#     column_width_mm = st.number_input("Column width (mm)", value=300, min_value=225)
#     column_length_mm = st.number_input("Column length (mm)", value=300, min_value=225)
#     bar_diameter_mm = st.number_input("Reinforcement Bar Diameter (mm)", value=12, min_value=6)
#     cover_mm = st.number_input("Enter concrete cover in mm:", value=50, min_value=20)
#     effective_depth = footing_depth - cover_mm - (bar_diameter_mm * 0.5) # mm
#     d_m = effective_depth / 1000 # m

#     critical_perimeter = 2 * (column_width_mm + column_length_mm) + (4 * math.pi * effective_depth)
#     Pcr = critical_perimeter

#     # Area within critical perimeter (a1 + 4d)(a2 + 4d) - (4 - pi)(2d^2)
#     col_width_m = column_width_mm / 1000
#     col_length_m = column_length_mm / 1000
#     critical_area = (col_width_m + 4 * d_m) * (col_width_m + 4 * d_m) - (4 - math.pi) * (2 * d_m)**2 
#     Acr = critical_area

#     column_side = col_width_m
#     perimeter = 4 * (col_width_m + 2 * 1.5 * effective_depth)  # d = effective_depth assumed
#     V = factored_load * 1e3  # Convert to N

#     b0 = 4 * (col_width_m + effective_depth)
#     v_ed = V / (b0 * effective_depth)
#     v_rd_c = 0.5 * (fcu ** 0.5)

#     footing_side_m = provided_footing_side_mm / 1000 # m

#     # Net pressure, fnet = 1.1W/1.4Aprov
#     net_upward_pressure = (1.1 * factored_load) / (1.4 * footing_side_m ** 2)
    
#     # Load causing punching is the total load outside the critical perimeter, V = fnet(base area - area within critical perimeter) kN
#     V_net_kN = net_upward_pressure * ((footing_side_m ** 2) - Acr)  # kN
#     V_net_N = V_net_kN * 1e3  # Convert to N
#     Vpunch = V_net_N / (Pcr * effective_depth)  # N/mm²
    
#     st.write(f"Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm")
#     st.write(f"Effective Depth (d): {effective_depth} mm")
#     st.write(f"Critical Perimeter (Pcr): {round(Pcr, 2)} mm")
#     st.write(f"Area within critical perimeter (Acr): {round(Acr, 4)} m²")
#     st.write(f"Punching shear stress (ved): {v_ed:.2f} N/mm²")
#     st.write(f"Punching shear capacity (vrdc): {v_rd_c:.2f} N/mm²")
#     st.write(f"Punching Shear Stress (Vpunch): {Vpunch:.3f} N/mm²")

#     if v_ed < v_rd_c:
#         st.success("Punching shear check PASSED.")
#     else:
#         st.error("Punching shear check FAILED.")

# # ----------------------------
# # 3. Moment & Reinforcement Tab
# # ----------------------------
# with tabs[2]:
#     st.header("Moment and Reinforcement Design")

#     provided_footing_side_m = provided_footing_side_mm / 1000  # m
#     overhang_m = (provided_footing_side_m - col_width_m) / 2  # m
#     Mx_kNm = 0.5 * net_upward_pressure * (overhang_m ** 2)  # kNm/m (Moment per unit width)
#     My_kNm = Mx_kNm  # Same due to square footing symmetry
#     st.write(f"Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm")
#     st.write(f"Factored moment (Mx = My): {My_kNm:.2f} kNm/m") # Corrected unit display

#     # Effective depth should ideally be calculated based on footing depth, cover, and bar diameter
#     # Using the value from Punching Shear for consistency, but consider a separate input or calculation if needed
#     effective_depth_mm = st.number_input("Effective Depth (d) for Moment (mm)", value=effective_depth, min_value=50.0)
#     fy_Nmm2 = fy # Using fy from the sidebar

#     # Eurocode 2 calculation for required steel area
#     fcd_Nmm2 = 0.85 * fcu / 1.5  # Design compressive strength of concrete (using fcu as fck approx.)
#     K = My_kNm * 1e6 / (fcd_Nmm2 * 1000 * effective_depth_mm**2) # b = 1000 mm for per meter width

#     K_bal = 0.167  # Approximate balanced K for concrete grade around C30 (EC2) - ADJUST IF NEEDED FOR YOUR fcu
#     if K > K_bal:
#         st.warning("Section requires compression reinforcement or increased depth based on simplified K_bal.")

#     la = effective_depth_mm * (0.5 + math.sqrt(0.25 - K / 1.134))  # Lever arm (z in EC2)
#     if la > 0.95 * effective_depth_mm:
#         la = 0.95 * effective_depth_mm

#     As_required = (My_kNm * 1e6) / (0.87 * fy_Nmm2 * la) # mm²/m (Required steel area per meter width)
#     st.write(f"Required reinforcement area (Ast): {As_required:.2f} mm²/m")

#     # Reinforcement Suggestion Logic with Preferred Spacings
#     bar_options = [12, 16, 20]
#     max_spacing = 300  # mm
#     min_spacing = 50   # mm
#     suitable_options = []
#     preferred_spacings = [100, 125, 150, 175, 200, 225, 250, 300]

#     for bar_dia in bar_options:
#         area_per_bar = (math.pi * bar_dia ** 2) / 4  # mm²
#         for n_bars in range(math.ceil(As_required / area_per_bar), 21): # Start with a reasonable lower bound for n_bars
#             spacing = 1000 / n_bars  # mm
#             Ast_provided_per_meter = n_bars * area_per_bar

#             if min_spacing <= spacing <= max_spacing and Ast_provided_per_meter >= As_required * 0.95: # Allow a small under-provision
#                 suitable_options.append({
#                     'bar_dia': bar_dia,
#                     'area_per_bar': round(area_per_bar, 2),
#                     'no_bars': n_bars,
#                     'Ast_provided_per_meter': round(Ast_provided_per_meter, 2),
#                     'spacing': round(spacing, 2)
#                 })

#     if suitable_options:
#         def get_spacing_preference_score(option):
#             min_diff = float('inf')
#             for sp in preferred_spacings:
#                 diff = abs(option['spacing'] - sp)
#                 if diff < min_diff:
#                     min_diff = diff
#             return min_diff

#         best_option = min(suitable_options, key=lambda x: (get_spacing_preference_score(x), abs(x['Ast_provided_per_meter'] - As_required)))

#         st.subheader("Reinforcement Suggestion:")
#         st.write(f"Bar Diameter: T{best_option['bar_dia']} mm")
#         st.write(f"Spacing: {best_option['spacing']} mm c/c")
#         st.write(f"Provided Ast: {best_option['Ast_provided_per_meter']} mm²/m")
#         st.write(f"Provide T{best_option['bar_dia']} mm bars @ {best_option['spacing']} mm c/c in both directions")

#         reinforcement_spacing = best_option['spacing']
#         bar_diameter_for_view = best_option['bar_dia']
#     else:
#         st.warning("No suitable reinforcement option found within spacing limits with sufficient steel area.")
#         st.write(f"Required Ast per meter: {As_required:.2f} mm²")

# # ... (Rest of your code)
# # ----------------------------
# # 4. 2D Plan View Tab
# # ----------------------------
# with tabs[3]:
#     st.header("2D Plan View")

#     # Ensure column dimensions are in meters
#     # col_size_m = col_size / 1000  # Assuming col_size is in mm from earlier input
#     # col_width_m = col_size_m  # For a square column
#     # col_length_m = col_size_m # For a square column

#     provided_footing_side_m = provided_footing_side_mm / 1000 # Ensure footing side is in meters

#     # Footing outline
#     x_footing = [0, 0, provided_footing_side_m, provided_footing_side_m, 0]
#     y_footing = [0, provided_footing_side_m, provided_footing_side_m, 0, 0]

#     # Column outline centered in footing
#     x_col = [
#         provided_footing_side_m/2 - col_width_m/2,
#         provided_footing_side_m/2 + col_width_m/2,
#         provided_footing_side_m/2 + col_width_m/2,
#         provided_footing_side_m/2 - col_width_m/2,
#         provided_footing_side_m/2 - col_width_m/2
#     ]
#     y_col = [
#         provided_footing_side_m/2 - col_length_m/2,
#         provided_footing_side_m/2 - col_length_m/2, 
#         provided_footing_side_m/2 + col_length_m/2,
#         provided_footing_side_m/2 + col_length_m/2,
#         provided_footing_side_m/2 - col_length_m/2
#     ]

#     # Create plot
#     fig_plan = go.Figure()
#     fig_plan.add_trace(go.Scatter(x=x_footing, y=y_footing, name='FOOTING', mode='lines', line=dict(color='red', width=1.5)))
#     fig_plan.add_trace(go.Scatter(x=x_col, y=y_col, name='COLUMN', mode='lines', line=dict(color='green', width=1.5)))

#     fig_plan.update_layout(
#         title_text='FOOTING PLAN',
#         width=500,
#         height=500,
#         xaxis=dict(title=f'{provided_footing_side_m:.2f} (m)', scaleanchor='y', scaleratio=1),
#         yaxis=dict(title=f'{provided_footing_side_m:.2f} (m)'),
#         showlegend=True
#     )
#     st.plotly_chart(fig_plan)
    
# # ----------------------------
# # 5. 3D Reinforcement View Tab
# # ----------------------------
# with tabs[4]:
#     st.header("3D Reinforcement View")
#     # Use the provided footing side and bar spacing for the 3D view
#     provided_side_mm_3d = st.number_input("Footing Side Length for 3D View (mm)", value=int(footing_side_mm_calculated), help="Visualize reinforcement in this size.")
#     reinforcement_spacing = st.number_input("Reinforcement Spacing (mm)", value=int(spacing) if 'spacing' in locals() else 150, min_value=50)
#     bar_positions_x = np.arange(50, provided_side_mm_3d, reinforcement_spacing)
#     bar_positions_y = np.arange(50, provided_side_mm_3d, reinforcement_spacing)
#     center_3d = provided_side_mm_3d / 2
#     col_half_3d = provided_side_mm_3d / 2

#     fig3d = go.Figure()
#     for x in bar_positions_x:
#         fig3d.add_trace(go.Scatter3d(x=[x, x], y=[0, provided_side_mm_3d], z=[0, 0],
#                                     mode='lines', line=dict(color='red', width=5), name='Bar X'))
#     for y in bar_positions_y:
#         fig3d.add_trace(go.Scatter3d(x=[0, provided_side_mm_3d], y=[y, y], z=[-10, -10],
#                                     mode='lines', line=dict(color='green', width=5), name='Bar Y'))
#     # Column block
#     fig3d.add_trace(go.Mesh3d(
#         x=[center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d,
#            center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d],
#         y=[center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d,
#            center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d],
#         z=[0, 0, 0, 0, 300, 300, 300, 300],
#         color='blue', opacity=0.5, name='Column', showscale=False
#     ))
#     fig3d.update_layout(title="3D Reinforcement View", scene=dict(
#         xaxis=dict(title='X (mm)'), yaxis=dict(title='Y (mm)'), zaxis=dict(title='Z (mm)'),
#         aspectratio=dict(x=1, y=1, z=0.3)
#     ))
#     st.plotly_chart(fig3d, use_container_width=True)

# import streamlit as st
# import plotly.graph_objects as go
# import numpy as np
# import math

# # --- Page configuration ---
# st.set_page_config(page_title="Square Pad Footing Design", layout="wide")

# # --- Define CSS styles ---
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("style.css")

# st.markdown("<div class='app-header'>Welcome to the design tool page.</div>", unsafe_allow_html=True)

# if st.button("Go to Home", key="home_button", use_container_width=False):
#     st.switch_page("landing_page.py")

# # --- Tabs setup ---
# tabs = st.tabs(["Project Overview", "Punching Shear Check", "Moment & Reinforcement", "2D Plan View", "3D Reinforcement View"])

# # ----------------------------
# # 1. Project Overview Tab
# # ----------------------------
# with tabs[0]:
#     st.title("Square Pad Footing Design")
#     st.markdown("""
#     This application performs the structural design of a square pad footing
#     supporting a centrally loaded square column based on Eurocode 2 provisions.

#     Enter your input parameters in the sidebar to get started.
#     """)

#     with st.sidebar:
#         st.header("Input Parameters")
#         dead_load = st.number_input("Dead Load (kN)", value=950.0)
#         imposed_load = st.number_input("Imposed Load (kN)", value=200.0)
#         fcu = st.number_input("Concrete Strength fcu (N/mm²)", value=35.0)
#         fy = st.number_input("Steel Yield Strength fy (N/mm²)", value=500.0)
#         safe_bearing = st.number_input("Safe Bearing Capacity (kN/m²)", value=170.0)

#     total_load = dead_load + imposed_load
#     factored_load = 1.35 * dead_load + 1.5 * imposed_load

#     # Calculate initial footing size based on factored load and bearing capacity
#     footing_area_calculated = 1.1 * factored_load / (1.4 * safe_bearing)  # in m²
#     footing_side_calculated = np.sqrt(footing_area_calculated)  # m
#     footing_side_mm_calculated = footing_side_calculated * 1000

#     st.write("### Summary of Inputs")
#     st.write(f"Total service load: {total_load:.2f} kN")
#     st.write(f"Factored load: {factored_load:.2f} kN")
#     st.write(f"Safe bearing capacity: {safe_bearing:.1f} kN/m²")
#     st.write(f"Calculated Footing Size (approx): {footing_side_mm_calculated:.0f} mm × {footing_side_mm_calculated:.0f} mm")

# # ----------------------------
# # 2. Punching Shear Check Tab
# # ----------------------------
# with tabs[1]:
#     st.header("Punching Shear Check")

#     provided_footing_side_mm = st.number_input("Provided Footing Side Length (mm)", value=int(footing_side_mm_calculated), help="Use the actual side length you will provide.")
#     footing_depth = st.number_input("Footing Depth (h) for Base (mm)", value=400, min_value=150)
#     column_width_mm = st.number_input("Column width (mm)", value=300, min_value=225)
#     column_length_mm = st.number_input("Column length (mm)", value=300, min_value=225)
#     bar_diameter_mm = st.number_input("Reinforcement Bar Diameter (mm)", value=12, min_value=6)
#     cover_mm = st.number_input("Enter concrete cover in mm:", value=50, min_value=20)
#     effective_depth = footing_depth - cover_mm - (bar_diameter_mm * 0.5)  # mm
#     d_m = effective_depth / 1000  # m

#     critical_perimeter = 2 * (column_width_mm + column_length_mm) + (4 * math.pi * effective_depth)
#     Pcr = critical_perimeter

#     # Area within critical perimeter (a1 + 4d)(a2 + 4d) - (4 - pi)(2d^2)
#     col_width_m = column_width_mm / 1000
#     col_length_m = column_length_mm / 1000
#     critical_area = (col_width_m + 4 * d_m) * (col_width_m + 4 * d_m) - (4 - math.pi) * (2 * d_m) ** 2
#     Acr = critical_area

#     column_side = col_width_m
#     perimeter = 4 * (col_width_m + 2 * 1.5 * effective_depth)  # d = effective_depth assumed
#     V = factored_load * 1e3  # Convert to N

#     b0 = 4 * (col_width_m + effective_depth)
#     v_ed = V / (b0 * effective_depth)
#     v_rd_c = 0.5 * (fcu ** 0.5)

#     footing_side_m = provided_footing_side_mm / 1000  # m

#     # Net pressure, fnet = 1.1W/1.4Aprov
#     net_upward_pressure = (1.1 * factored_load) / (1.4 * footing_side_m ** 2)

#     # Load causing punching is the total load outside the critical perimeter, V = fnet(base area - area within critical perimeter) kN
#     V_net_kN = net_upward_pressure * ((footing_side_m ** 2) - Acr)  # kN
#     V_net_N = V_net_kN * 1e3  # Convert to N
#     Vpunch = V_net_N / (Pcr * effective_depth)  # N/mm²

#     st.write(f"Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm")
#     st.write(f"Effective Depth (d): {effective_depth} mm")
#     st.write(f"Critical Perimeter (Pcr): {round(Pcr, 2)} mm")
#     st.write(f"Area within critical perimeter (Acr): {round(Acr, 4)} m²")
#     st.write(f"Punching shear stress (ved): {v_ed:.2f} N/mm²")
#     st.write(f"Punching shear capacity (vrdc): {v_rd_c:.2f} N/mm²")
#     st.write(f"Punching Shear Stress (Vpunch): {Vpunch:.3f} N/mm²")

#     if v_ed < v_rd_c:
#         st.success("Punching shear check PASSED.")
#     else:
#         st.error("Punching shear check FAILED.")

# # ----------------------------
# # 3. Moment & Reinforcement Tab
# # ----------------------------
# with tabs[2]:
#     st.header("Moment and Reinforcement Design")

#     provided_footing_side_m = provided_footing_side_mm / 1000  # m
#     overhang_m = (provided_footing_side_m - column_width_m) / 2  # m
#     Mx_kNm = 0.5 * net_upward_pressure * (overhang_m ** 2)  # kNm/m (Moment per unit width)
#     My_kNm = Mx_kNm  # Same due to square footing symmetry
#     st.write(f"Provided Footing Size: {provided_footing_side_mm:.0f} mm × {provided_footing_side_mm:.0f} mm")
#     st.write(f"Factored moment (Mx = My): {My_kNm:.2f} kNm/m")  # Corrected unit display

#     # Effective depth should ideally be calculated based on footing depth, cover, and bar diameter
#     # Using the value from Punching Shear for consistency, but consider a separate input or calculation if needed
#     effective_depth_mm = st.number_input("Effective Depth (d) for Moment (mm)", value=effective_depth, min_value=50.0)
#     fy_Nmm2 = fy  # Using fy from the sidebar

#     # Eurocode 2 calculation for required steel area
#     fcd_Nmm2 = 0.85 * fcu / 1.5  # Design compressive strength of concrete (using fcu as fck approx.)
#     K = My_kNm * 1e6 / (fcd_Nmm2 * 1000 * effective_depth_mm ** 2)  # b = 1000 mm for per meter width

#     K_bal = 0.167  # Approximate balanced K for concrete grade around C30 (EC2) - ADJUST IF NEEDED FOR YOUR fcu
#     if K > K_bal:
#         st.warning("Section requires compression reinforcement or increased depth based on simplified K_bal.")

#     la = effective_depth_mm * (0.5 + math.sqrt(0.25 - K / 1.134))  # Lever arm (z in EC2)
#     if la > 0.95 * effective_depth_mm:
#         la = 0.95 * effective_depth_mm

#     As_required = (My_kNm * 1e6) / (0.87 * fy_Nmm2 * la)  # mm²/m (Required steel area per meter width)
#     st.write(f"Required reinforcement area (Ast): {As_required:.2f} mm²/m")

#     # Reinforcement Suggestion Logic with Preferred Spacings
#     bar_options = [12, 16, 20]
#     max_spacing = 300  # mm
#     min_spacing = 50  # mm
#     suitable_options = []
#     preferred_spacings = [100, 125, 150, 175, 200, 225, 250, 300]

#     for bar_dia in bar_options:
#         area_per_bar = (math.pi * bar_dia ** 2) / 4  # mm²
#         for n_bars in range(math.ceil(As_required / area_per_bar), 21):  # Start with a reasonable lower bound for n_bars
#             spacing = 1000 / n_bars  # mm
#             Ast_provided_per_meter = n_bars * area_per_bar

#             if min_spacing <= spacing <= max_spacing and Ast_provided_per_meter >= As_required * 0.95:  # Allow a small under-provision
#                 suitable_options.append({
#                     'bar_dia': bar_dia,
#                     'area_per_bar': round(area_per_bar, 2),
#                     'no_bars': n_bars,
#                     'Ast_provided_per_meter': round(Ast_provided_per_meter, 2),
#                     'spacing': round(spacing, 2)
#                 })

#     if suitable_options:
#         def get_spacing_preference_score(option):
#             min_diff = float('inf')
#             for sp in preferred_spacings:
#                 diff = abs(option['spacing'] - sp)
#                 if diff < min_diff:
#                     min_diff = diff
#             return min_diff

#         best_option = min(suitable_options, key=lambda x: (
#             get_spacing_preference_score(x), abs(x['Ast_provided_per_meter'] - As_required)))

#         st.subheader("Reinforcement Suggestion:")
#         st.write(f"Bar Diameter: T{best_option['bar_dia']} mm")
#         st.write(f"Spacing: {best_option['spacing']} mm c/c")
#         st.write(f"Provided Ast: {best_option['Ast_provided_per_meter']} mm²/m")
#         st.write(f"Provide T{best_option['bar_dia']} mm bars @ {best_option['spacing']} mm c/c in both directions")

#         reinforcement_spacing = best_option['spacing']
#         bar_diameter_for_view = best_option['bar_dia']
#     else:
#         st.warning("No suitable reinforcement option found within spacing limits with sufficient steel area.")
#         st.write(f"Required Ast per meter: {As_required:.2f} mm²")

# # ----------------------------
# # 4. 2D Plan View Tab
# # ----------------------------
# with tabs[3]:
#     st.header("2D Plan View")

#     provided_footing_side_m = provided_footing_side_mm / 1000  # Ensure footing side is in meters

#     # Footing outline
#     x_footing = [0, 0, provided_footing_side_m, provided_footing_side_m, 0]
#     y_footing = [0, provided_footing_side_m, provided_footing_side_m, 0, 0]

#     # Column outline centered in footing
#     x_col = [
#         provided_footing_side_m / 2 - column_width_m / 2,
#         provided_footing_side_m / 2 + column_width_m / 2,
#         provided_footing_side_m / 2 + column_width_m / 2,
#         provided_footing_side_m / 2 - column_width_m / 2,
#         provided_footing_side_m / 2 - column_width_m / 2
#     ]
#     y_col = [
#         provided_footing_side_m / 2 - column_length_m / 2,
#         provided_footing_side_m / 2 - column_length_m / 2,
#         provided_footing_side_m / 2 + column_length_m / 2,
#         provided_footing_side_m / 2 + column_length_m / 2,
#         provided_footing_side_m / 2 - column_length_m / 2
#     ]

#     # Create plot
#     fig_plan = go.Figure()
#     fig_plan.add_trace(go.Scatter(x=x_footing, y=y_footing, name='FOOTING', mode='lines', line=dict(color='red', width=1.5)))
#     fig_plan.add_trace(go.Scatter(x=x_col, y=y_col, name='COLUMN', mode='lines', line=dict(color='green', width=1.5)))

#     fig_plan.update_layout(
#         title_text='FOOTING PLAN',
#         width=500,
#         height=500,
#         xaxis=dict(title=f'{provided_footing_side_m:.2f} (m)', scaleanchor='y', scaleratio=1),
#         yaxis=dict(title=f'{provided_footing_side_m:.2f} (m)'),
#         showlegend=True
#     )
#     st.plotly_chart(fig_plan)

# # ----------------------------
# # 5. 3D Reinforcement View Tab
# # ----------------------------
# with tabs[4]:
#     st.header("3D Reinforcement View")
#     # Use the provided footing side and bar spacing for the 3D view
#     provided_side_mm_3d = st.number_input("Footing Side Length for 3D View (mm)",
#                                          value=int(footing_side_mm_calculated),
#                                          help="Visualize reinforcement in this size.")
#     reinforcement_spacing = st.number_input("Reinforcement Spacing (mm)",
#                                          value=int(reinforcement_spacing) if 'reinforcement_spacing' in locals() else 150,
#                                          min_value=50)
#     bar_positions_x = np.arange(0, provided_side_mm_3d + reinforcement_spacing, reinforcement_spacing)  # Ensure 0 and end are included
#     bar_positions_y = np.arange(0, provided_side_mm_3d + reinforcement_spacing, reinforcement_spacing)
#     center_3d = provided_side_mm_3d / 2
#     col_half_3d = column_width_mm / 2  # Use column_width_mm

#     fig3d = go.Figure()

#     # X-direction bars (running along Y-axis)
#     for x in bar_positions_x:
#         fig3d.add_trace(go.Scatter3d(
#             x=[x, x],
#             y=[0, provided_side_mm_3d],
#             z=[0, 0],
#             mode='lines',
#             line=dict(color='red', width=3),  # Reduced width for clarity
#             name='X-Bars'  # Added name for legend
#         ))

#     # Y-direction bars (running along X-axis)
#     for y in bar_positions_y:
#         fig3d.add_trace(go.Scatter3d(
#             x=[0, provided_side_mm_3d],
#             y=[y, y],
#             z=[0, 0],
#             mode='lines',
#             line=dict(color='green', width=3),
#             name='Y-Bars'
#         ))

#     # Column block - corrected and simplified
#     fig3d.add_trace(go.Mesh3d(
#         x=[center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d,
#            center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d, center_3d - col_half_3d],
#         y=[center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d,
#            center_3d - col_half_3d, center_3d - col_half_3d, center_3d + col_half_3d, center_3d + col_half_3d],
#         z=[0, 0, 0, 0, 300, 300, 300, 300],
#         color='blue',
#         opacity=0.5,
#         name='Column',
#         showscale=False  # Remove color scale
#     ))

#     fig3d.update_layout(
#         title="3D Reinforcement View",
#         scene=dict(
#             xaxis=dict(title='X (mm)', range=[0, provided_side_mm_3d]),  # Added range for better view
#             yaxis=dict(title='Y (mm)', range=[0, provided_side_mm_3d]),
#             zaxis=dict(title='Z (mm)', range=[0, 300]),  # Added range for Z
#             aspectratio=dict(x=1, y=1, z=0.3),
#             camera=dict(
#                 eye=dict(x=1.2, y=1.2, z=0.8)  # Adjust camera position for better view
#             )
#         ),
#         showlegend=True  # Show legend to distinguish X and Y bars
#     )

#     st.plotly_chart(fig3d, use_container_width=True)

