import streamlit as st


# Function to generate accordion sections based on the offering type
def generate_accordion(offering_type):
    if offering_type == "Meal Kit":
        sections = {
            "Sample Menu": """
            ##### From <MONTH OR MENU TITLE/THEME>
            * **Dish 1 Name** — Dish 1 Description
            * **Dish 2 Name** — Dish 2 Description
            * …
            * **Pantry Items**

            All meals come fully prepared with accompanying Chef's notes & prep instructions — **simply assemble & serve**.
            """,

            "Additional Perks": f"""
            Your <PARTNER NAME> membership also includes:
            * 10% off retail
            * ...

            **INTERNAL NOTE**: If no substantive "additional perks", don't include this section, e.g. no need to highlight things like:
            * Chef's notes
            * "First to know about xyz"
            *
            """,

            "How Membership Works": "You can **skip a month, pause or cancel your membership anytime** via your Table22 member portal.",

            "Who You’re Supporting": "... Stuff about the Chef/establishment from the PLP"
        }
    else:
        sections = {
            "Section 1": "Details for Section 1...",
            "Section 2": "Details for Section 2..."
        }
    return sections

# Streamlit app layout
st.title("PDP Guidelines & Best Practices")
with st.expander(label="Overview", expanded=True):
    st.markdown("""### Overview""")
    # with st.expander("Goals:"):
    st.markdown("""
    This tool aims to provide an **up-to-date guide for creating high-quality & _standardized_ PDPs quickly**.
    It will be updated as we test into further best practices (e.g. what accordion sections to include, what copy to use, what types of photos to highlight, etc.)

    Currently, it povides guidance on:
    * Default **copy for variant choices** (the dropdowns/boxes users have to select)
    * Recommended **accordion sections** to include along w/ default copy (will be updated as we test into / out of others)
    * **Image gallery guidelines**

    The recommendations will be tailored to the offering type (e.g. meal kit vs. wine club), though currently **only meal kit guidelines have been implemented**.
    """)
with st.expander("""High-Level Guidelines"""):
    st.markdown("""
    #### High-Level Guidelines
    1. Use the "Radio Box" structure for variant choices (the selections users have to make)
    2. Concise copy, presented at the decision point
        - 1 liner describing the offering in the top "The Experience" section
        - Relevant info for add-ons w/in the add-on section (not in accordions)
    3. Accordions to Include (for a Meal Kit):
        - Sample Menu
        - How Membership Works
        - Additional Perks (BUT ONLY IF THEY'RE MEANINGFUL)
        - Who You're Supporting
    4. Aim for 4 to 5 high quality **food** photos
    5. Include no more than 8 TOTAL photos
    6. Make an **appealing** sample menu — ask yourself: "Does this feel like a good value? Would I buy this?"
    7. Use **bolding** & _italics_ to convey meaning — imagine a user only reads the bolded words, is that a coherent messsage?
    """)

with st.expander(label="Image Gallery Guidelines", expanded=False):
    st.markdown("### Photo Guidelines for Food Offering")
    # with st.expander("See guidelines:"):
    st.markdown("""
    1. Include **4 to 5** QUALITY photos of **food**
        - 3:4 aspect ratio (configure the cropping when uploading)
        - Not blurry (check on desktop)
        - Consider using an instagram photo downloader tool, e.g. https://toolzu.com/downloader/instagram/photo/, to get all the photos from an insta account
    2. When choosing photos:
        - Lead w/ more universally appealling dishes — pastas & chicken parms vs. fish
        - Lead w/ a protein or star dish vs. a dessert or salad
        - Avoid dishes that are ill-suited for at-home, e.g. "tweezer" dishes reliant on plating, raw dishes (ceviches & tartares),
        - If you have a sample menu, try to have some photos map to that
    3. Include a photo of the Chef/Owner/Team/space towards the end
    4. If delivery is available, include a photo of the delivery map towards the end
    5. Make sure you have no more than 8 total photos.

    """)

with st.expander(label="Sample PDPs to Reference", expanded=False):
    st.markdown("### Meal Kits")
    # with st.expander("See guidelines:"):
    st.markdown("""
    1. Red Hen / All Purpose — https://app.table22.com/product/redhen-allpurpose-chefs-dinner-club
    2. Cardamom — https://app.table22.com/product/cardamom-dinner-club
    3. Scratch & Co. — https://app.table22.com/product/scratch-co-supper-club
    """)


st.markdown("### Copy Guide")

st.markdown("##### Enter Basic Info")
partner_name = st.text_input("Partner Name")
# Offering type selection
offering_type = st.selectbox("Offering Type", ["Meal Kit", "OTHER'S NOT IMPLEMENTED YET"])
# if offering_type == "Meal Kit":
#     chefs_name = st.text_input("Chef's Name")
# offering_type = st.("Select the type of offering", ["Meal Kit"])


# Display variant choices based on offering type
# variant_choices = get_variant_choices(offering_type)
st.markdown("#### Variant Choices")
with st.expander(label="Guidelines", expanded=False):
    st.markdown("""
    ###### Guidelines
    1. Use "Radio Box" variant selectors
    2. Keep copy concise, use bolding to increase skimmability
    3. Give users the info they need _at the point they're making a decision_, e.g. tell them what the beverage pairing or "pantry-add-on" entails when they're deciding whether to click the add on.
    """)

with st.expander("Primary Offering Section", expanded=True):
    st.write("##### The Experience")
    st.text_area(
        "Create a concise one-liner to describe the offering. Emphasize what makes it UNIQUE and SPECIAL.",
        f"Each month Chef [CHEF'S NAME] and our culinary team bring you a **rotating multi-course tasting menu featuring** [UNIQUE DIFFERENTIATOR].",
        # placeholder=f"signature {partner_name} dishes, new inspirations, and special off-menu chef’s creations."
        )
    st.write(f"""

    """)
    st.radio("Note the format of the choices here:", ["For 2 ($X)", "For 4 ($Y)"], horizontal=True)

with st.expander("Beverage Add-Ons", expanded=False):
    st.write("##### Beverage Add-Ons")
    bev_pairing_type = st.radio(
        "Which type of Bev. Pairing are we offering?",
        ["None", "Wine", "Cocktail", "Assortment"],
        horizontal=True,
        )
    if bev_pairing_type != "None":
        with st.container(border=True):

            bev_copy = {
                "Wine": dict(
                    title='Wine',
                    desc="Tailored to each month's menu.",
                    choices=["No, Thank You", "1 Bottle (+$X)", "2 Bottles (+$Y)"]

                ),
                "Cocktail": dict(
                    title="Cocktail",
                    desc="",
                    choices=["No, Thank You", "For 2 (+$X)", "For 4 (+$Y)"]
                ),
                "Assortment": dict(
                    title="Beverage",
                    desc="A monthly curation of wine, cocktails, or whatever we’re feeling — selected to pair with the month’s dishes!",
                    choices=["No, Thank You", "For 2 (+$X)", "For 4 (+$Y)"]
                ),
            }

            st.write(f"##### Optional {bev_copy.get(bev_pairing_type).get('title')} Pairing")
            st.write(bev_copy.get(bev_pairing_type).get('desc'))
            st.radio("Note the format of the choices here:", bev_copy.get(bev_pairing_type).get('choices'), horizontal=True)

with st.expander("Other Add-Ons", expanded=False):
    st.write("##### Food Add-Ons")
    food_addons = st.toggle("Offer food add-ons?")
    # https://app.table22.com/product/anju-chiko-dinner-series-new
    if food_addons:
        st.markdown("Describe what the food add-on(s) are w/in the the section. E.g. see https://app.table22.com/product/anju-chiko-dinner-series-new")
        # food_addon_type = st.text_input("What kind?")

with st.expander("Fulfillment Type", expanded=True):
    st.write("##### Fulfillment Type")
    ff_types = st.multiselect(
        "Which fulfillment types are we offering?",
        ["Pickup", "Delivery",  "Extended Delivery", "Shipping"]
        )
    if ff_types == ['Pickup', 'Delivery']:
        st.write("##### Pickup or Delivery?")
        st.radio(
            "", ["Pickup", "Delivery (+$15)"],
            captions=["Pickup at {ADDRESS}", "See delivery range in photos"],
            horizontal=True
    )

# Generate and display accordion sections based on offering type
accordion_sections = generate_accordion(offering_type)
# with st.expander(label="Accordions", expanded=True):
st.markdown("### Accordion Sections")
for title, content in accordion_sections.items():
    with st.expander(title):
        st.write(content)
