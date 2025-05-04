<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Standard History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <!-- Mobile Header (from application-list.html) -->
      <MobileHeader />
      <div id="i2m428p" class="middle-content"> <!-- Scroll wrapper -->
        <h1><i class="fa-solid fa-search"></i> Sàng lọc CV</h1>
        <div class="job-selection shadow-border">
          <label for="job-opening-select">Chọn Tin Tuyển dụng:</label>
          <select type="text" id="job-opening-select" class="shadow-border">
            <option>-- Chọn Tin Tuyển dụng --</option>
            <option value="job1" selected>Senior Software Engineer (JOB/001)</option>
            <option value="job2">Marketing Manager (JOB/002)</option>
          </select>
          <div id="isz9rtf" class="job-criteria">(Tiêu chí: Java, Spring Boot, AWS, 5+ năm kinh nghiệm)</div>
        </div>
        <h2><i class="fa-solid fa-sitemap"></i> Danh sách Ứng viên</h2>
        <!-- Action Bar -->
        <div id="iukhnlu" class="action-bar">
          <div class="filters">
            <label for="filter-screen-status">Trạng thái:</label>
            <select type="text" id="filter-screen-status" class="shadow-border">
              <option>Tất cả</option>
              <option>Mới</option>
              <option>Đang xem xét</option>
              <option>Phù hợp</option>
              <option>Không phù hợp</option>
            </select>
            <input type="text" placeholder="Tìm theo Tên ứng viên..." class="shadow-border"/>
          </div>
          <div class="buttons">
            <button type="button" class="success"><i class="fa-solid fa-robot"></i> Sàng lọc bằng AI</button>
            <button type="button" id="iluafp2" class="primary"><i class="fa-solid fa-check-circle"></i> Chọn phỏng vấn</button>
            <button type="button" class="secondary"><i class="fa-solid fa-envelope"></i> Gửi email từ chối</button> <!-- Example Bulk Action -->
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th><input type="checkbox"/></th>
              <th>Tên ứng viên</th>
              <th>Ngày nộp</th>
              <th>Nguồn</th>
              <th>CV</th>
              <th>Trạng thái Sàng lọc</th>
              <th>Điểm/Xếp hạng (AI)</th>
              <th>Ghi chú/Nhận xét AI</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Nguyễn Văn A</a></td>
              <td>2025-04-19</td>
              <td id="i22x1pb">Form ERPNext</td>
              <td><a href="#"><i class="fa-solid fa-users"></i> Xem CV</a></td>
              <td><span class="status-badge status-fit">Phù hợp</span></td>
              <td>9/10</td>
              <td>
                Phù hợp: Kinh nghiệm 5 năm Java, Spring Boot. Có chứng chỉ AWS.
                <span class="ai-notes">(AI Suggestion)</span>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Trần Thị B</a></td>
              <td>2025-04-20</td>
              <td>Google Form</td>
              <td><a href="#"><i class="fa-solid fa-users"></i> Xem CV</a></td>
              <td><span class="status-badge status-review">Đang xem xét</span></td>
              <td>7/10</td>
              <td>
                Cần xem xét: Kinh nghiệm Java 3 năm, chưa có kinh nghiệm AWS rõ ràng.
                <span class="ai-notes">(AI Suggestion)</span>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Lê Văn C</a></td>
              <td>2025-04-18</td>
              <td>Form ERPNext</td>
              <td><a href="#"><i class="fa-solid fa-users"></i> Xem CV</a></td>
              <td><span class="status-badge status-unfit">Không phù hợp</span></td>
              <td>4/10</td>
              <td>
                Không phù hợp: Thiếu kinh nghiệm Spring Boot.
                <span class="ai-notes">(AI Suggestion - User Confirmed)</span>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Phạm Thị D</a></td>
              <td>2025-04-20</td>
              <td>ITviec (Manual Upload)</td>
              <td><a href="#"><i class="fa-solid fa-users"></i> Xem CV</a></td>
              <td><span class="status-badge status-new">Mới</span></td>
              <td>N/A</td>
              <td>Chưa sàng lọc</td>
            </tr>
            <!-- More rows -->
          </tbody>
        </table>
        <!-- Pagination -->
        <div class="pagination">
          <span class="disabled shadow-border">«</span>
          <span class="current shadow-border">1</span>
          <a href="#" class="shadow-border">2</a>
          <a href="#" class="shadow-border">3</a>
          <a href="#" class="shadow-border">»</a>
        </div>
      </div> <!-- End middle-content -->
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySection from '@/components/ChatHistorySection.vue';
import TabSection from '@/components/TabSection.vue';
import MobileHeader from '../components/MobileHeader.vue';

// View-specific logic can go here
</script>

<!-- No scoped styles -->