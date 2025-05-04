<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="ia2z4h9" class="middle-content"> <!-- Scroll wrapper -->
        <h1><i id="i2nmkgb" class="fa-solid fa-calendar-alt"></i> Lên lịch &amp; Quản lý Phỏng vấn</h1>
        <h2><i class="fa-solid fa-list"></i> Danh sách Lịch phỏng vấn</h2> <!-- Corrected icon -->
        <!-- Action Bar -->
        <div class="action-bar">
          <div class="filters">
            <label for="filter-int-status">Trạng thái:</label>
            <select type="text" id="filter-int-status" class="shadow-border">
              <option>Tất cả</option>
              <option>Đã lên lịch</option>
              <option>Đã hoàn thành</option>
              <option>Đã hủy</option>
            </select>
            <label for="filter-int-job">Vị trí:</label>
            <select type="text" id="filter-int-job" class="shadow-border">
              <option>Tất cả</option>
              <option>Senior Software Engineer</option>
              <option>Marketing Manager</option>
            </select>
            <input type="date" id="filter-int-date" class="shadow-border"/>
            <input type="text" placeholder="Tìm theo Tên ứng viên..." class="shadow-border"/>
          </div>
          <div class="buttons">
            <button type="button"><i class="fa-solid fa-plus"></i> Lên lịch Phỏng vấn mới</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th><input type="checkbox"/></th>
              <th>Ứng viên</th>
              <th>Vị trí</th>
              <th>Ngày giờ</th>
              <th>Người phỏng vấn</th>
              <th>Trạng thái</th>
              <th>Kết quả</th>
              <th>Hành động</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Nguyễn Văn A</a></td>
              <td>Senior Software Engineer</td>
              <td>2025-04-22 10:00</td>
              <td>Trần Văn D</td>
              <td><span class="status-badge status-completed">Đã hoàn thành</span></td>
              <td><span class="result-pass">Đạt</span></td>
              <td class="row-actions">
                <button type="button" title="Xem Kết quả"><i class="fa-solid fa-poll-h"></i></button>
                <button type="button" title="Gửi Offer"><i class="fa-solid fa-gift"></i></button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Trần Thị B</a></td>
              <td>Senior Software Engineer</td>
              <td>2025-04-23 14:00</td>
              <td>Trần Văn D, Lê Thị E</td>
              <td><span class="status-badge status-scheduled">Đã lên lịch</span></td>
              <td><span class="result-pending">Chưa có</span></td>
              <td class="row-actions">
                <button type="button" title="Xem Chi tiết"><i class="fa-solid fa-eye"></i></button>
                <button type="button" title="Sửa lịch"><i class="fa-solid fa-edit"></i></button>
                <button type="button" title="Hủy lịch"><i class="fa-solid fa-calendar-times"></i></button>
                <button type="button" title="Nhập Kết quả"><i class="fa-solid fa-clipboard-check"></i></button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Hoàng Văn F</a></td>
              <td>Marketing Manager</td>
              <td>2025-04-21 09:00</td>
              <td>Nguyễn Thị G</td>
              <td><span class="status-badge status-completed">Đã hoàn thành</span></td>
              <td><span class="result-fail">Không đạt</span></td>
              <td class="row-actions">
                <button type="button" title="Xem Kết quả"><i class="fa-solid fa-poll-h"></i></button>
                <button type="button" title="Gửi Email Từ chối"><i class="fa-solid fa-envelope"></i></button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Vũ Thị H</a></td>
              <td>Senior Software Engineer</td>
              <td>2025-04-20 15:00</td>
              <td>Trần Văn D</td>
              <td><span class="status-badge status-canceled">Đã hủy</span></td>
              <td>N/A</td>
              <td class="row-actions">
                <button type="button" title="Xem Chi tiết"><i class="fa-solid fa-eye"></i></button>
              </td>
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
import ChatHistorySection from '../components/ChatHistorySection.vue';
import MobileHeader from '../components/MobileHeader.vue';
import TabSection from '../components/TabSection.vue';

// Component logic goes here if needed
</script>