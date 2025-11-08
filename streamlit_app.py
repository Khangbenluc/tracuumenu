import streamlit as st
import datetime

# --- Dữ liệu Thực đơn (Thêm thủ công theo ngày cụ thể) ---
# CẬP NHẬT: Các ngày đầu tiên của khoảng (vd: 02-11-2025-03-11-2025) được xác định là KHÔNG có món ăn cố định.
SPECIFIC_MENU_DATA = {
    # Các ngày KHÔNG có món ăn cố định (Đã cập nhật mô tả tiếng Anh sang "Day off")
    datetime.date(2025, 11, 2): {"option": "KHÔNG CÓ", "dish_vi": "không có món ăn (ngày nghỉ)", "calories": "N/A", "dish_en": "No meal available (Day off)"},
    datetime.date(2025, 11, 9): {"option": "KHÔNG CÓ", "dish_vi": "không có món ăn (ngày nghỉ)", "calories": "N/A", "dish_en": "No meal available (Day off)"},
    datetime.date(2025, 11, 16): {"option": "KHÔNG CÓ", "dish_vi": "không có món ăn (ngày nghỉ)", "calories": "N/A", "dish_en": "No meal available (Day off)"},
    datetime.date(2025, 11, 23): {"option": "KHÔNG CÓ", "dish_vi": "không có món ăn (ngày nghỉ)", "calories": "N/A", "dish_en": "No meal available (Day off)"},
    
    # Các ngày CÓ món ăn
    datetime.date(2025, 11, 3): {"option": "LỰA CHỌN 1", "dish_vi": "BÚN DỌC MÙNG HẢI SẢN", "calories": "575 kcal", "dish_en": "SEAFOOD DOUBLE TAPE NOODLES"},
    datetime.date(2025, 11, 4): {"option": "LỰA CHỌN 3", "dish_vi": "PHILE CÁ BASA KHO TỘ & BÒ XÀO ỚT CHUÔNG", "calories": "350 kcal & 250 kCal", "dish_en": "BRAISED BASA FISH FILLET & STIR-FRIED BEEF WITH BELL PEPPER"},
    datetime.date(2025, 11, 5): {"option": "LỰA CHỌN 2", "dish_vi": "MÌ XÀO HẢI SẢN + SÚP CUA", "calories": "1000 kcal", "dish_en": "SEAFOOD NOODLES & CRAB SOUP"},
    datetime.date(2025, 11, 6): {"option": "LỰA CHỌN 3", "dish_vi": "THỊT KHO TIÊU & MỰC XÀO CẢI THÌA SỐT DẦU HÀO", "calories": "350 kcal & 350 kcal", "dish_en": "BRAISED PORK WITH PEPPER & STIR-FRIED SQUID WITH BOK CHOY, OYSTER SAUCE"},
    datetime.date(2025, 11, 7): {"option": "LỰA CHỌN 3", "dish_vi": "SALAD BÒ MÈ RANG & TRỨNG SỐT THỊT BẰM", "calories": "440 kcal & 270 kCal", "dish_en": "ROASTED BEEF SALAD & STEAMED EGGS WITH MINCED MEAT"},
    datetime.date(2025, 11, 10): {"option": "LỰA CHỌN 4", "dish_vi": "MÓN CHAY", "calories": "700 kcal", "dish_en": "VEGETARIAN MENU"},
    datetime.date(2025, 11, 11): {"option": "LỰA CHỌN 3", "dish_vi": "BÒ NẤU TIÊU & ĐẬU HỦ THỊT BẰM SỐT DẦU HÀO", "calories": "300 kcal & 350 kcal", "dish_en": "BEEF STEW WITH GREEN PEPPER & TOFU WITH PORK BALL AND OYSTER SAUCE"},
    datetime.date(2025, 11, 12): {"option": "LỰA CHỌN 2", "dish_vi": "CƠM BA RỌI CHIÊN MẮM TỎI", "calories": "900kcal", "dish_en": "VIETNAMESE FRIED PORK BELLY WITH GARLIC AND FISH SAUCE"},
    datetime.date(2025, 11, 13): {"option": "LỰA CHỌN 2", "dish_vi": "HỦ TIẾU TRỘN XÁ XÍU & SÚP GÀ XÉ", "calories": "850 kcal", "dish_en": "NOODLE MIXED CHAR SIU + CHICKEN SOUP"},
    datetime.date(2025, 11, 14): {"option": "LỰA CHỌN 3", "dish_vi": "CÁ BASA CHIÊN MẮM SẢ & THỊT HEO XÀO SU SU", "calories": "370kcal & 295 kcal", "dish_en": "FRIED BASA FISH FILLET WITH LEMONGRASS AND FISH SAUCE & CHAYOTE WITH PORK"},
    datetime.date(2025, 11, 17): {"option": "LỰA CHỌN 2", "dish_vi": "PAD THÁI BÒ TRỨNG", "calories": "675 kcal", "dish_en": "PAD THAI BEEF AND EGG"},
    datetime.date(2025, 11, 18): {"option": "LỰA CHỌN 3", "dish_vi": "SƯỜN RAM SỐT CHANH DÂY & TRỨNG CUỘN XÚC XÍCH", "calories": "340 kcal & 250 kcal", "dish_en": "CARAMELIZED PORK RIBS WITH PASSION FRUIT SAUCE & SAUSAGE EGG ROLL"},
    datetime.date(2025, 11, 19): {"option": "LỰA CHỌN 3", "dish_vi": "GÀ CHIÊN NƯỚC MẮM & THỊT XÀO NẤM BÀO NGƯ", "calories": "420 kcal & 202 kcal", "dish_en": "FRIED CHICKEN WITH FISH SAUCE & STIR-FRIED PORK WITH OYSTER MUSHROOM"},
    datetime.date(2025, 11, 20): {"option": "LỰA CHỌN 3", "dish_vi": "BÒ XÀO NẤM & ĐẬU HỦ DỒN THỊT SỐT CÀ", "calories": "300kCal & 250 kCal", "dish_en": "STIR-FRIED BEEF WITH MUSHROOM & STUFFED TOFU IN TOMATO SAUCE"},
    datetime.date(2025, 11, 21): {"option": "LỰA CHỌN 4", "dish_vi": "MÓN CHAY", "calories": "700 kcal", "dish_en": "VEGETARIAN MENU"},
    datetime.date(2025, 11, 24): {"option": "LỰA CHỌN 3", "dish_vi": "LAGU BÒ & GIÁ HẸ XÀO THỊT ĐẬU HỦ", "calories": "400 kCal & 295 kcal", "dish_en": "BEEF RAGOUT & STIR-FRIED TOFU WITH PORK, BEAN SPROUTS, CHIVES"},
    datetime.date(2025, 11, 25): {"option": "LỰA CHỌN 3", "dish_vi": "THỊT KHO TIÊU & CÁ ĐIÊU HỒNG CHIÊN SỐT MẮM GỪNG", "calories": "350kcal & 400 kcal", "dish_en": "BRAISED PORK WITH PEPPER & FRIED RED TILAPIA WITH GINGER FISH SAUCE"},
    datetime.date(2025, 11, 26): {"option": "LỰA CHỌN 4", "dish_vi": "MÓN CHAY", "calories": "700 kcal", "dish_en": "VEGETARIAN MENU"},
    datetime.date(2025, 11, 27): {"option": "LỰA CHỌN 2", "dish_vi": "MÌ XÀO HẢI SẢN + SÚP CUA", "calories": "1000 kcal", "dish_en": "SEAFOOD NOODLES & CRAB SOUP"},
    datetime.date(2025, 11, 28): {"option": "LỰA CHỌN 1", "dish_vi": "CÀ RI GÀ + BÁNH MÌ", "calories": "672 kcal", "dish_en": "CHICKEN CURRY BREAD"},
}

def get_vietnamese_weekday(date_obj):
    """
    Chuyển đổi đối tượng datetime thành tên thứ trong tuần bằng tiếng Việt (Thứ Hai, Chủ Nhật).
    """
    # weekday() trả về 0 cho Thứ Hai, 6 cho Chủ Nhật
    weekday_map = {
        0: "Thứ Hai", 1: "Thứ Ba", 2: "Thứ Tư", 3: "Thứ Năm",
        4: "Thứ Sáu", 5: "Thứ Bảy", 6: "Chủ Nhật"
    }
    return weekday_map.get(date_obj.weekday(), "Không xác định")

# --- Ứng dụng Streamlit Chính ---
st.set_page_config(
    page_title="Tra Cứu Thực Đơn",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("🍽️ Tra Cứu Thực Đơn Hàng Ngày (Tháng 11/2025)")
st.markdown("Chọn ngày bạn muốn tra cứu để xem thực đơn đã được cập nhật theo danh sách mới nhất!")

# 1. Yêu cầu người dùng nhập ngày hiện tại (hoặc ngày bất kỳ)
# Đặt ngày mặc định là một ngày có menu (ví dụ: 04/11/2025) để người dùng dễ xem
default_date = datetime.date(2025, 11, 4) if datetime.date(2025, 11, 4) in SPECIFIC_MENU_DATA else datetime.date.today()

selected_date = st.date_input(
    "Vui lòng chọn ngày",
    default_date,
    min_value=datetime.date(2025, 11, 2),
    max_value=datetime.date(2025, 11, 28),
    help="Chọn một ngày."
)

if selected_date:
    day_name = get_vietnamese_weekday(selected_date)

    st.header(f"📅 Thực đơn cho ngày {selected_date.strftime('%d/%m/%Y')} ({day_name})")

    # 2. Tra cứu menu dựa trên ngày cụ thể
    menu = SPECIFIC_MENU_DATA.get(selected_date)

    if menu:
        if menu['option'] == "KHÔNG CÓ":
            # Xử lý trường hợp không có menu cố định
            st.error(f"❌ Ngày {selected_date.strftime('%d/%m/%Y')}: **{menu['dish_vi'].upper()}**")
            st.info("Đây là ngày nghỉ nên không có món ăn. Vui lòng chọn ngày khác!")
        else:
            # Xử lý trường hợp có menu
            # Chỉ hiển thị thông tin chung về Lựa chọn
            st.subheader(f"🎉 Chi tiết Thực đơn cho Lựa chọn {menu['option'].split()[-1]}")
            
            # --- 1. Món ăn Tiếng Việt (Full Width, #00FF7F - Spring Green) ---
            st.markdown(f"""
            <div style='background-color: #00FF7F; padding: 12px; border-radius: 10px; margin-top: 5px; margin-bottom: 20px;'>
                <p style='font-weight: bold; margin-bottom: 5px; color: #000000;'>Tên món ăn (Tiếng Việt):</p>
                <p style='color: #000000; font-style: bold; font-size: 16px;'>{menu["dish_vi"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # 2. Tên tiếng Anh/Mô tả (Full Width, #00FFFF - Cyan)
            st.markdown(f"""
            <div style='background-color: #00FFFF; padding: 12px; border-radius: 10px; margin-top: 5px; margin-bottom: 20px;'>
                <p style='font-weight: bold; margin-bottom: 5px; color: #000000;'>Mô tả / Tên tiếng Anh (English Description):</p>
                <p style='color: #000000; font-style: bold; font-size: 16px;'>{menu["dish_en"]}</p>
            </div>
            """, unsafe_allow_html=True)

            # 3. Calo và Lựa chọn (2 cột bằng nhau)
            col1, col2 = st.columns(2)

            with col1:
                # Dùng st.metric để hiển thị Calo. Chuỗi Calo dài sẽ tự động điều chỉnh.
                st.metric("🔥 Calo ước tính", menu["calories"])
                
            with col2:
                # Dùng st.metric để hiển thị Lựa chọn
                st.metric("✨ Lựa chọn", menu["option"].split()[-1])
            
    else:
        st.warning(f"Không tìm thấy thực đơn cho ngày {selected_date.strftime('%d/%m/%Y')}. Vui lòng chọn một ngày khác!")

st.markdown("---")
st.caption("Tra cứu thực đơn tháng 11")
