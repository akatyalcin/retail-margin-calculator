import customtkinter as ctk

# Temel ayarlar
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x600")
app.title("Margin & Inventory Calculator")

# --- DİL SÖZLÜĞÜ (DICTIONARY) ---
translations = {
    "TR": {
        "title": "Mağaza Stok Analitiği",
        "cost_ph": "Birim Maliyet (örn., 250.50)",
        "price_ph": "Satış Fiyatı (örn., 599.90)",
        "stock_ph": "Stok Adedi (örn., 150)",
        "btn_calc": "Metrikleri Hesapla",
        "awaiting": "Giriş bekleniyor...",
        "error": "Hata: Lütfen geçerli sayılar girin.",
        "gross": "Brüt Kâr (Ürün Başı)",
        "margin": "Kâr Marjı",
        "total": "Toplam Stok Değeri"
    },
    "EN": {
        "title": "Store Inventory Analytics",
        "cost_ph": "Unit Cost (e.g., 250.50)",
        "price_ph": "Retail Price (e.g., 599.90)",
        "stock_ph": "Stock Quantity (e.g., 150)",
        "btn_calc": "Calculate Metrics",
        "awaiting": "Awaiting input...",
        "error": "Error: Please enter valid numbers.",
        "gross": "Gross Profit (Per Item)",
        "margin": "Profit Margin",
        "total": "Total Retail Value"
    }
}

current_lang = "TR" # Varsayılan dil

# Dil değiştirme fonksiyonu
def change_language(choice):
    global current_lang
    current_lang = choice
    lang_data = translations[choice]
    
    # Arayüzdeki metinleri anında güncelle
    label_title.configure(text=lang_data["title"])
    entry_cost.configure(placeholder_text=lang_data["cost_ph"])
    entry_price.configure(placeholder_text=lang_data["price_ph"])
    entry_stock.configure(placeholder_text=lang_data["stock_ph"])
    btn_calculate.configure(text=lang_data["btn_calc"])
    
    # Hesaplama yapılmadıysa bekleme metnini güncelle
    if "₺" not in result_text.get() and "%" not in result_text.get():
        result_text.set(lang_data["awaiting"])

# Finansal hesaplama fonksiyonu
def calculate_metrics():
    lang_data = translations[current_lang]
    try:
        cost = float(entry_cost.get())
        price = float(entry_price.get())
        stock = int(entry_stock.get())

        # Matematiksel işlemler
        profit_per_item = price - cost
        profit_margin = (profit_per_item / price) * 100
        total_retail_value = price * stock

        # Seçili dile göre sonucu yazdırma
        result_text.set(
            f"{lang_data['gross']}: {profit_per_item:.2f} ₺\n"
            f"{lang_data['margin']}: %{profit_margin:.2f}\n"
            f"{lang_data['total']}: {total_retail_value:,.2f} ₺"
        )
    except ValueError:
        result_text.set(lang_data["error"])

# --- ARAYÜZ (UI) TASARIMI ---

# Dil Seçici (Segmented Button)
lang_selector = ctk.CTkSegmentedButton(app, values=["TR", "EN"], command=change_language)
lang_selector.pack(pady=15)
lang_selector.set("TR") # Başlangıçta TR seçili olsun

# Başlık
label_title = ctk.CTkLabel(app, text=translations["TR"]["title"], font=("Helvetica", 24, "bold"))
label_title.pack(pady=20)

# Girdi Kutuları
entry_cost = ctk.CTkEntry(app, placeholder_text=translations["TR"]["cost_ph"], width=250, height=40)
entry_cost.pack(pady=10)

entry_price = ctk.CTkEntry(app, placeholder_text=translations["TR"]["price_ph"], width=250, height=40)
entry_price.pack(pady=10)

entry_stock = ctk.CTkEntry(app, placeholder_text=translations["TR"]["stock_ph"], width=250, height=40)
entry_stock.pack(pady=10)

# Hesapla Butonu
btn_calculate = ctk.CTkButton(app, text=translations["TR"]["btn_calc"], command=calculate_metrics, width=250, height=45, font=("Helvetica", 16, "bold"))
btn_calculate.pack(pady=25)

# Sonuç Gösterim Alanı
result_text = ctk.StringVar()
result_text.set(translations["TR"]["awaiting"])
label_result = ctk.CTkLabel(app, textvariable=result_text, font=("Helvetica", 16), justify="left", text_color="#00FF00")
label_result.pack(pady=10)

app.mainloop()
