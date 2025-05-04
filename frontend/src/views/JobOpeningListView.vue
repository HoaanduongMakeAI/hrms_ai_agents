<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div class="middle-content"> <!-- Scroll wrapper -->
        <h1><i class="fa-solid fa-bullhorn"></i> Quản lý Đăng tin Tuyển dụng</h1>
        <h2><i class="fa-solid fa-list"></i> Danh sách Tin Tuyển dụng</h2> <!-- Corrected icon -->
        <!-- Action Bar -->
        <div class="action-bar">
          <div class="filters">
            <label for="filter-status">Trạng thái:</label>
            <select type="text" id="filter-status" class="shadow-border">
              <option>Tất cả</option>
              <option>Nháp</option>
              <option>Đang đăng</option>
              <option>Đã đóng</option>
            </select>
            <label for="filter-dept">Phòng ban:</label>
            <select type="text" id="filter-dept" class="shadow-border">
              <option>Tất cả</option>
              <option>IT</option>
              <option>Marketing</option>
            </select>
            <input type="text" placeholder="Tìm theo Tiêu đề công việc..." class="shadow-border"/>
          </div>
          <div class="buttons">
            <button type="button"><i class="fa-solid fa-plus"></i> Tạo Tin Tuyển dụng</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th><input type="checkbox"/></th>
              <th>Tiêu đề công việc</th>
              <th>Trạng thái</th>
              <th>Ngày tạo</th>
              <th>Nền tảng đã đăng</th>
              <th>Số lượng ứng viên</th>
              <th>Hành động</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Senior Software Engineer</a></td>
              <td><span class="status-badge status-posting">Đang đăng</span></td>
              <td>2025-04-18</td>
              <td>
                Facebook <span class="platform-status platform-success">(Thành công)</span><br/>
                ITviec <span class="platform-status platform-error">(Lỗi Login)</span><br/>
                LinkedIn <span class="platform-status platform-success">(Thành công)</span>
              </td>
              <td>5</td>
              <td class="row-actions">
                <button type="button" title="Xem"><i class="fa-solid fa-eye"></i></button>
                <button type="button" title="Sửa"><i class="fa-solid fa-edit"></i></button>
                <button type="button" title="Đăng lại"><i class="fa-solid fa-redo"></i></button>
                <button type="button" title="Đóng"><i class="fa-solid fa-times-circle"></i></button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Marketing Manager</a></td>
              <td><span class="status-badge status-draft">Nháp</span></td>
              <td>2025-04-20</td>
              <td>Chưa đăng</td>
              <td>0</td>
              <td class="row-actions">
                <button type="button" title="Xem"><i class="fa-solid fa-eye"></i></button>
                <button type="button" title="Sửa"><i class="fa-solid fa-edit"></i></button>
                <button type="button" title="Đăng"><i class="fa-solid fa-paper-plane"></i></button>
                <button type="button" title="Xóa"><i class="fa-solid fa-trash"></i></button>
              </td>
            </tr>
            <tr>
              <td><input type="checkbox"/></td>
              <td><a href="#">Junior Frontend Developer</a></td>
              <td><span class="status-badge status-closed">Đã đóng</span></td>
              <td>2025-03-10</td>
              <td>
                TopCV <span class="platform-status platform-success">(Thành công)</span><br/>
                VietnamWorks <span class="platform-status platform-success">(Thành công)</span>
              </td>
              <td>15</td>
              <td class="row-actions">
                <button type="button" title="Xem"><i class="fa-solid fa-eye"></i></button>
                <button type="button" title="Lưu trữ"><i class="fa-solid fa-archive"></i></button>
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