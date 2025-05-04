<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader /> <!-- Mobile Header Section -->
      <div id="i22tyof" class="middle-content"> <!-- Scroll wrapper -->
        <h1><i class="fa-solid fa-search"></i> Sàng lọc CV</h1>
        <h2><i class="fa-solid fa-user-check"></i> Chi tiết Ứng viên &amp; Sàng lọc</h2>
        <p id="i4nrumb">Tin tuyển dụng: <a href="#">Senior Software Engineer (JOB/001)</a></p>
        <div class="form-view-container">
          <!-- Phần Trái - Trình xem CV (CV Viewer Area) -->
          <div id="iije24f" class="cv-viewer-area shadow-border">
            <h3><i class="fa-solid fa-file-pdf"></i> CV: Nguyễn Văn A</h3>
            <div id="iex4f3h" class="cv-viewer-placeholder">
              CV Viewer Placeholder<br/>
              (Hiển thị nội dung PDF/DOCX hoặc dữ liệu Form `Job Applicant`)
              <br/><br/><em>(Thanh công cụ viewer: Zoom, Download, etc.)</em>
            </div>
          </div>
          <!-- Phần Phải - Khu vực Sàng lọc (Screening Details Area) -->
          <div id="iuk9bjf" class="screening-details-area shadow-border">
            <h3><i class="fa-solid fa-tasks"></i> Thông tin Sàng lọc</h3>
            <!-- Section Phân tích AI -->
            <div class="ai-analysis-section">
              <h4><i class="fa-solid fa-brain"></i> Phân tích AI</h4>
              <p><strong>Thông tin trích xuất:</strong></p>
              <ul>
                <li>Kỹ năng khớp: Java (5 năm), Spring Boot (4 năm), AWS (Chứng chỉ)</li>
                <li>Kinh nghiệm liên quan: Project Lead tại XYZ Corp (3 năm)</li>
                <li>Học vấn nổi bật: Đại học Bách Khoa (Loại Giỏi)</li>
              </ul>
              <p><strong>Điểm số/Xếp hạng đề xuất:</strong> 9/10 (Phù hợp)</p>
              <p id="ivqp5z2"><strong>Lý do/Nhận xét chi tiết:</strong> Đáp ứng đầy đủ các yêu cầu chính về kỹ năng và kinh nghiệm. Có chứng chỉ AWS là điểm cộng.</p>
            </div>
            <!-- Section Đánh giá thủ công -->
            <div class="manual-screening-section">
              <h4><i class="fa-solid fa-user-edit"></i> Đánh giá thủ công</h4>
              <div class="form-group">
                <label for="manual-status">Trạng thái sàng lọc</label>
                <select type="text" id="manual-status" class="shadow-border">
                  <option value="new">Mới</option>
                  <option value="review">Đang xem xét</option>
                  <option value="fit" selected>Phù hợp</option>
                  <option value="unfit">Không phù hợp</option>
                </select>
              </div>
              <div class="form-group">
                <label for="manual-score">Điểm số/Xếp hạng (Thủ công)</label>
                <input type="text" id="manual-score" placeholder="Nhập điểm hoặc xếp hạng" value="9/10" class="shadow-border"/>
              </div>
              <div id="i0m7hmq" class="form-group">
                <label for="manual-notes">Ghi chú thủ công</label>
                <textarea id="manual-notes" placeholder="Nhập nhận xét, đánh giá riêng..." class="shadow-border">Ứng viên tiềm năng, cần kiểm tra kỹ về kinh nghiệm AWS thực tế.</textarea>
              </div>
              <div id="imxrsuv" class="form-actions">
                <button type="button" class="primary"><i class="fa-solid fa-save"></i> Lưu thay đổi</button>
              </div>
            </div>
            <!-- Action Buttons for Applicant -->
            <div class="screening-actions">
              <button type="button" id="i50g0za" class="secondary"><i class="fa-solid fa-envelope"></i> Gửi email từ chối</button>
              <button type="button" id="ihxe1qt" class="success"><i class="fa-solid fa-calendar-plus"></i> Lên lịch phỏng vấn</button>
            </div>
          </div>
        </div>
      </div> <!-- End middle-content -->
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySection from '../components/ChatHistorySection.vue';
import TabSection from '../components/TabSection.vue';
import MobileHeader from '../components/MobileHeader.vue';

// Component logic goes here if needed
</script>