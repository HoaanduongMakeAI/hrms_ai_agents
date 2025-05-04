<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div class="middle-content"> <!-- Scroll wrapper -->
        <h1><i class="fa-solid fa-calendar-alt"></i> Lên lịch &amp; Quản lý Phỏng vấn</h1>
        <h2><i class="fa-solid fa-edit"></i> Lên lịch/Chi tiết Phỏng vấn (Interview Doctype)</h2>
        <!-- Section: Thông tin Ứng viên -->
        <div id="i8q0txk" class="form-section shadow-border">
          <h3><i class="fa-solid fa-user"></i> Thông tin Ứng viên</h3>
          <div class="form-grid">
            <div class="form-group">
              <label>Ứng viên</label>
              <a href="#" class="readonly-link">Trần Thị B (Link to Job Applicant)</a>
            </div>
            <div class="form-group">
              <label>Vị trí ứng tuyển</label>
              <input type="text" value="Senior Software Engineer" readonly="" class="shadow-border"/>
            </div>
          </div>
        </div>
        <!-- Section: Thông tin Lịch trình -->
        <div class="form-section shadow-border">
          <h3><i class="fa-solid fa-clock"></i> Thông tin Lịch trình</h3>
          <div class="form-grid">
            <div id="ic7bopd" class="form-group">
              <label for="interview-round">Vòng phỏng vấn/Giai đoạn</label>
              <input type="text" id="interview-round" placeholder="e.g., Vòng 1, Vòng Kỹ thuật" class="shadow-border"/>
            </div>
            <div class="form-group">
              <label for="interviewers">Người phỏng vấn</label>
              <select type="text" id="interviewers" multiple class="shadow-border">
                <option selected>Trần Văn D</option>
                <option>Lê Thị E</option>
                <!-- Link Field (Multi-select) -->
              </select>
            </div>
            <div class="form-group">
              <label for="interview-date">Ngày phỏng vấn</label>
              <input type="date" id="interview-date" class="shadow-border"/>
            </div>
            <div id="ilrej65" class="form-group">
              <div id="ifab1ag">
                <label for="start-time">Giờ bắt đầu</label>
                <input type="time" id="start-time" class="shadow-border"/>
              </div>
              <div id="izzx4w3">
                <label for="end-time">Giờ kết thúc</label>
                <input type="time" id="end-time" class="shadow-border"/>
              </div>
            </div>
            <div id="ikpvu21" class="ai-suggestion-area gjs-grid-column"> <!-- Initially hidden, shown after AI suggestion -->
              <h4>Khung giờ đề xuất:</h4>
              <ul>
                <li>2025-04-23 14:00 - 15:00</li>
                <li>2025-04-24 10:00 - 11:00</li>
              </ul>
              <button type="button" id="inm8vwh" class="primary">Chọn</button>
            </div>
            <div class="form-group">
              <label for="interview-type">Hình thức phỏng vấn</label>
              <select type="text" id="interview-type" class="shadow-border">
                <option>Online</option>
                <option>Trực tiếp</option>
              </select>
            </div>
            <div class="form-group">
              <label for="location-link">Địa điểm/Link Online</label>
              <input type="text" id="location-link" placeholder="Nhập địa điểm hoặc link Google Meet/Zoom..." class="shadow-border"/>
            </div>
            <div class="form-group">
              <button type="button" class="ai-button"><i class="fa-solid fa-magic"></i> Đề xuất (AI)</button>
            </div>
          </div>
        </div>
        <!-- Section: Hỗ trợ Phỏng vấn -->
        <div id="i7iq6nq" class="form-section shadow-border">
          <h3><i class="fa-solid fa-question-circle"></i> Hỗ trợ Phỏng vấn (Tùy chọn)</h3>
          <button class="ai-button gjs-grid-column"><i class="fa-solid fa-magic"></i> Gợi ý câu hỏi (AI)</button>
          <div id="i5jhs3e" class="ai-suggestion-area gjs-grid-column">
            <h4>Câu hỏi gợi ý:</h4>
            <textarea readonly="" id="ijengqz" class="shadow-border">- Describe your experience with Spring Boot microservices.
- How would you handle conflicting requirements?
- What are your salary expectations?
(Placeholder for AI generated questions)</textarea>
          </div>
        </div>
        <!-- Section: Ghi chú/Phản hồi Phỏng vấn -->
        <div class="form-section shadow-border">
          <h3><i class="fa-solid fa-comments"></i> Ghi chú/Phản hồi Phỏng vấn</h3>
          <div class="feedback-section gjs-grid-column">
            <label>Phản hồi từ: Trần Văn D</label>
            <textarea placeholder="Nhập nhận xét, đánh giá chi tiết..." class="shadow-border"></textarea>
            <!-- Optional rating/score fields -->
          </div>
          <div class="feedback-section gjs-grid-column">
            <label>Phản hồi từ: Lê Thị E</label>
            <textarea placeholder="Nhập nhận xét, đánh giá chi tiết..." class="shadow-border"></textarea>
          </div>
          <button class="secondary add-feedback-btn gjs-grid-column"><i class="fa-solid fa-plus"></i> Thêm người phản hồi</button>
        </div>
        <!-- Section: Kết quả Phỏng vấn -->
        <div class="form-section shadow-border">
          <h3><i class="fa-solid fa-check-double"></i> Kết quả Phỏng vấn</h3>
          <div class="form-grid">
            <div class="form-group">
              <label for="decision">Quyết định</label>
              <select type="text" id="decision" class="shadow-border">
                <option>-- Chọn kết quả --</option>
                <option value="accept">Chấp nhận</option>
                <option value="reject">Từ chối</option>
                <option value="next_round">Cần phỏng vấn thêm/Chờ vòng sau</option>
              </select>
            </div>
            <div id="ilsg1mi" class="form-group"> <!-- Span across grid -->
              <label for="decision-notes">Ghi chú quyết định</label>
              <textarea id="decision-notes" placeholder="Lý do cho quyết định..." class="shadow-border"></textarea>
            </div>
          </div>
        </div>
        <!-- Action Buttons -->
        <div class="form-actions">
          <button class="danger gjs-grid-column"><i class="fa-solid fa-trash"></i> Hủy lịch</button>
          <button class="secondary gjs-grid-column"><i class="fa-solid fa-save"></i> Lưu</button>
          <button class="primary gjs-grid-column"><i class="fa-solid fa-paper-plane"></i> Gửi thông báo mời</button>
          <button class="warning gjs-grid-column"><i class="fa-solid fa-envelope"></i> Gửi thông báo kết quả</button>
        </div>
      </div> <!-- End middle-content -->
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySection from '../components/ChatHistorySection.vue';
import MobileHeader from '../components/MobileHeader.vue';
import TabSection from '../components/TabSection.vue';

// Component logic goes here if needed
</script>