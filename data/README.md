# Data Directory

ไฟล์ข้อมูลในโฟลเดอร์นี้**ไม่ได้ถูก commit ขึ้น Git** เนื่องจากขนาดใหญ่เกินไป

## โครงสร้าง

```
data/
├── bronze/    # ข้อมูลดิบ (Raw) — ดาวน์โหลดจากแหล่งภายนอก
├── silver/    # ข้อมูลที่ผ่านการ clean (generated จาก pipeline)
└── gold/      # ข้อมูล aggregated พร้อมใช้ (generated จาก pipeline)
```

## วิธีได้ข้อมูล Bronze

ดาวน์โหลด Olist E-Commerce Dataset จาก Kaggle:  
🔗 https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

แล้ววางไฟล์ CSV ทั้งหมดไว้ที่ `data/bronze/olist/`

### ไฟล์ที่ต้องการ

| ไฟล์ | ขนาด |
|------|------|
| olist_orders_dataset.csv | 17 MB |
| olist_order_items_dataset.csv | 15 MB |
| olist_order_payments_dataset.csv | 5.5 MB |
| olist_order_reviews_dataset.csv | 14 MB |
| olist_customers_dataset.csv | 8.6 MB |
| olist_products_dataset.csv | 2.3 MB |
| olist_sellers_dataset.csv | 171 KB |
| olist_geolocation_dataset.csv | 58 MB |
| product_category_name_translation.csv | 2.6 KB |

## แผนในอนาคต

ข้อมูล Bronze จะย้ายไปเก็บบน **Azure Blob Storage**  
และจะมี script สำหรับดึงข้อมูลลงมาอัตโนมัติ (เร็วๆ นี้)
