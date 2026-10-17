# REA-AGENT — Sigverify System

ระบบตรวจสอบและยืนยันเอกสารพร้อมลายเซ็นดิจิทัล ตามมาตรฐานความปลอดภัยระดับสูง

## คุณสมบัติหลัก
- ✅ ตรวจสอบลายเซ็นดิจิทัล
- ✅ บันทึกประวัติแบบไม่สามารถแก้ไขย้อนหลังได้
- ✅ ปฏิบัติตามหลักการ **Fail-Closed**
- ✅ รองรับ Cosign Keyless Signing
- ✅ สอดคล้องกับมาตรฐาน **SLSA Level 3**

## โครงสร้างโฟลเดอร์,
REA-AGENT/
├── src/sigverify/ # โค้ดหลัก
├── scripts/ # สคริปต์ทดสอบ
├── policies/ # กฎและนโยบาย
├── k8s/ # ไฟล์ปรับใช้
└── .github/workflows # CI/CD
plaintext

## เริ่มใช้งาน
bash
# ติดตั้งแพ็กเกจ
pip install -r requirements.txt

# รันทดสอบ
make test
ความปลอดภัย
ดูรายละเอียดเพิ่มใน SECURITY.md และ COMPLIANCE.md
