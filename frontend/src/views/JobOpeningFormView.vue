<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div class="middle-content"> <!-- Scroll wrapper -->
        <h1><i class="fa-solid fa-bullhorn"></i> Quản lý Đăng tin Tuyển dụng</h1>
        <h2 id="ivn91y2"><i class="fa-solid fa-edit"></i> Tạo/Chỉnh sửa Tin Tuyển dụng (Job Opening)</h2>
        <!-- Section: Thông tin cơ bản -->
        <div class="form-section shadow-border">
          <h3><i class="fa-solid fa-info-circle"></i> Thông tin cơ bản</h3>
          <div class="form-grid">
            <div class="form-group">
              <label for="job-title">Tiêu đề công việc</label>
              <input type="text" id="job-title" placeholder="e.g., Senior Software Engineer" class="shadow-border"/>
            </div>
            <div class="form-group">
              <label for="department-2">Phòng ban</label> <!-- Changed id to department-2 to avoid conflict -->
              <select type="text" id="department-2" class="shadow-border">
                <option>-- Chọn phòng ban --</option>
                <option>IT</option>
                <option>Marketing</option>
              </select> <!-- Link Field -->
            </div>
            <div class="form-group">
              <label for="location">Địa điểm làm việc</label>
              <input type="text" id="location" placeholder="e.g., Đà Nẵng" class="shadow-border"/>
            </div>
            <div class="form-group">
              <label for="job-type">Loại hình công việc</label>
              <select type="text" id="job-type" class="shadow-border">
                <option>Full-time</option>
                <option>Part-time</option>
                <option>Contract</option>
              </select>
            </div>
            <div class="form-group">
              <label for="salary-range">Khoảng lương (Tùy chọn)</label>
              <input type="text" id="salary-range" placeholder="e.g., 15,000,000 - 25,000,000 VND" class="shadow-border"/>
            </div>
          </div>
        </div>
        <!-- Section: Nội dung Tin tuyển dụng -->
        <div class="form-section shadow-border">
          <h3><i class="fa-solid fa-file-alt"></i> Nội dung Tin tuyển dụng</h3> <!-- Corrected icon -->
          <div class="form-group">
            <label for="job-description">Mô tả công việc</label>
            <textarea id="job-description" placeholder="Nhập mô tả công việc..." class="shadow-border"></textarea>
            <!-- Rich Text Editor would be applied here -->
          </div>
          <div class="form-group">
            <label for="job-requirements">Yêu cầu ứng viên</label>
            <textarea id="job-requirements" placeholder="Nhập yêu cầu..." class="shadow-border"></textarea>
            <!-- Rich Text Editor would be applied here -->
          </div>
          <div class="form-group">
            <label for="job-benefits">Quyền lợi</label>
            <textarea id="job-benefits" placeholder="Nhập quyền lợi..." class="shadow-border"></textarea>
            <!-- Rich Text Editor would be applied here -->
          </div>
          <button type="button" class="ai-button"><i class="fa-solid fa-magic"></i> Tạo nội dung bằng AI</button>
          <div class="placeholder-ai-output">AI Output/Suggestion Area (Placeholder)</div>
        </div>
        <!-- Section: Nền tảng Đăng tin -->
        <div id="i0n33uk" class="form-section shadow-border">
          <h3><i class="fa-solid fa-share-alt"></i> Nền tảng Đăng tin</h3>
          <div class="form-group">
            <h4><i class="fa-solid fa-plug"></i> Đăng qua API</h4>
            <div class="platform-list">
              <div class="platform-item">
                <input type="checkbox" id="platform-fb" value="facebook"/>
                <label for="platform-fb"><i class="fab fa-facebook"></i> Facebook</label>
                <a href="#" class="config-link">(Cấu hình)</a>
                <span class="platform-status-indicator status-pending">Chưa đăng</span>
              </div>
              <div class="platform-item">
                <input type="checkbox" id="platform-x" value="x"/>
                <label for="platform-x"><i class="fab fa-twitter"></i> X/Twitter</label>
                <a href="#" class="config-link">(Cấu hình)</a>
                <span class="platform-status-indicator status-success">Đã đăng</span>
              </div>
              <div class="platform-item">
                <input type="checkbox" id="platform-li" value="linkedin" checked/>
                <label for="platform-li"><i class="fab fa-linkedin"></i> LinkedIn</label>
                <a href="#" class="config-link">(Cấu hình)</a>
                <span class="platform-status-indicator status-error">Lỗi API</span>
              </div>
              <!-- Add more platforms -->
            </div>
            <p class="config-note">Lưu ý: Thông tin xác thực (API keys) cần được quản lý an toàn.</p>
          </div>
          <div class="form-group">
            <h4><i class="fa-solid fa-desktop"></i> Đăng tự động (Playwright)</h4>
            <div class="platform-list">
              <div class="platform-item">
                <input type="checkbox" id="platform-itv" value="itviec" checked/>
                <label for="platform-itv"><i class="fa-solid fa-laptop-code"></i> ITviec</label>
                <a href="#" class="config-link">(Cấu hình Login)</a>
                <span class="platform-status-indicator status-pending">Đang chờ...</span>
              </div>
              <div class="platform-item">
                <input type="checkbox" id="platform-vnw" value="vnworks"/>
                <label for="platform-vnw"><i class="fa-solid fa-briefcase"></i> VietnamWorks</label>
                <a href="#" class="config-link">(Cấu hình Login)</a>
                <span class="platform-status-indicator status-pending">Chưa đăng</span>
              </div>
              <div class="platform-item">
                <input type="checkbox" id="platform-topcv" value="topcv"/>
                <label for="platform-topcv"><i class="fa-solid fa-file-invoice"></i> TopCV</label>
                <a href="#" class="config-link">(Cấu hình Login)</a>
                <span class="platform-status-indicator status-pending">Chưa đăng</span>
              </div>
              <!-- Add more platforms -->
            </div>
            <p class="config-note">Lưu ý: Thông tin đăng nhập cần được quản lý an toàn.</p>
          </div>
          <div class="placeholder-ai-output">Overall Posting Progress/Status (Placeholder)</div>
        </div>
        <!-- Section: Form Ứng tuyển -->
        <div id="ivggusk" class="form-section shadow-border">
          <h3><i class="fa-solid fa-clipboard-list"></i> Form Ứng tuyển</h3>
          <div class="form-group radio-group">
            <div>
              <input type="radio" id="form-erp-new" name="application_form_method" value="erp_new" v-model="applicationFormMethod"/>
              <label for="form-erp-new">Tạo Form mới trên ERPNext (Job Application Form)</label>
            </div>
            <div>
              <input type="radio" id="form-erp-ai" name="application_form_method" value="erp_ai" v-model="applicationFormMethod"/>
              <label for="form-erp-ai">Tạo Form mới với AI (Job Application Form)</label>
            </div>
            <div>
              <input type="radio" id="form-google" name="application_form_method" value="google" v-model="applicationFormMethod"/>
              <label for="form-google">Liên kết Form Google</label>
              <input v-if="applicationFormMethod === 'google'" type="text" id="google-form-link" placeholder="Dán link Google Form vào đây" class="nested-input shadow-border" v-model="googleFormLink"/>
            </div>
            <div>
              <input type="radio" id="form-ms" name="application_form_method" value="ms" v-model="applicationFormMethod"/>
              <label for="form-ms">Liên kết Form Microsoft</label>
              <input v-if="applicationFormMethod === 'ms'" type="text" id="ms-form-link" placeholder="Dán link Microsoft Form/SharePoint vào đây" class="nested-input shadow-border" v-model="msFormLink"/>
            </div>
            <div>
              <input type="radio" id="form-erp-existing" name="application_form_method" value="erp_existing" v-model="applicationFormMethod"/>
              <label for="form-erp-existing">Chọn Form ERPNext có sẵn (Job Application Form)</label>
              <select v-if="applicationFormMethod === 'erp_existing'" id="erp-existing-select" class="nested-select shadow-border" v-model="erpExistingForm">
                <option value="">-- Chọn Form --</option>
                <option value="form1">Form Tuyển dụng Chung</option>
                <option value="form2">Form Kỹ sư Phần mềm</option>
              </select>
            </div>
          </div>
          <div v-if="finalFormLinkDisplay" id="final-form-link" class="form-link-display">
            <strong>Link Form sẽ sử dụng:</strong> <a :href="finalFormLinkDisplay" target="_blank">{{ finalFormLinkDisplay }}</a>
          </div>
        </div>
        <!-- Action Buttons -->
        <div class="form-actions">
          <button type="button" class="secondary"><i class="fa-solid fa-save"></i> Lưu nháp</button>
          <button type="button" class="info"><i class="fa-solid fa-paper-plane"></i> Đăng tin</button>
          <button type="button" class="secondary"><i class="fa-solid fa-times"></i> Hủy bỏ</button>
        </div>
      </div> <!-- End middle-content -->
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import ChatHistorySection from '../components/ChatHistorySection.vue';
import TabSection from '../components/TabSection.vue';
import MobileHeader from '../components/MobileHeader.vue';

const applicationFormMethod = ref('erp_new'); // Default selection
const googleFormLink = ref('');
const msFormLink = ref('');
const erpExistingForm = ref('');

const finalFormLinkDisplay = computed(() => {
  switch (applicationFormMethod.value) {
    case 'erp_new':
      return 'http://example.com/erp-form/newly-created-form-id'; // Simulate link
    case 'erp_ai':
      return 'http://example.com/erp-form/ai-created-form-id'; // Simulate link
    case 'google':
      return googleFormLink.value || null; // Show only if link is entered
    case 'ms':
      return msFormLink.value || null; // Show only if link is entered
    case 'erp_existing':
      return erpExistingForm.value ? `http://example.com/erp-form/${erpExistingForm.value}` : null; // Show only if form is selected
    default:
      return null;
  }
});

// No onMounted needed as v-if handles initial state and computed handles updates
</script>