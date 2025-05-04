<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="ivhhhh-3" class="middle-content">
        <!-- Action Bar -->
        <div class="action-bar gjs-grid-row">
          <div class="filters gjs-grid-column">
            <label for="review-period-filter">Period:</label>
            <select type="text" id="review-period-filter" class="shadow-border">
              <option value="">All</option>
              <option value="q2-2025">Q2 2025</option>
              <option value="q1-2025">Q1 2025</option>
            </select>
            <label for="status-filter">Status:</label>
            <select type="text" id="status-filter" class="shadow-border">
              <option value="">All</option>
              <option value="not-started">Chưa bắt đầu</option>
              <option value="in-progress">Đang tiến hành</option>
              <option value="pending-confirm">Chờ xác nhận</option>
              <option value="completed">Đã hoàn thành</option>
            </select>
            <label for="dept-filter">Department:</label>
            <select type="text" id="dept-filter" class="shadow-border">
              <option value="">All</option>
              <option value="it">IT</option>
              <option value="sales">Sales</option>
              <option value="hr">Human Resources</option>
            </select>
          </div>
          <div class="search gjs-grid-column">
            <input type="text" placeholder="Search by Employee or Period..." class="shadow-border"/>
          </div>
          <div class="buttons gjs-grid-column">
            <button type="button" class="secondary"><i class="fa-solid fa-filter"></i> Apply Filters</button>
            <button type="button" class="primary"><i class="fa-solid fa-plus"></i> Start New Review</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th>Review Period</th>
              <th>Employee Name</th>
              <th>Position</th>
              <th>Department</th>
              <th>Review Status</th>
              <th>Review Date</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Q2 2025</td>
              <td>Nguyễn Văn A</td>
              <td>Software Engineer</td>
              <td>IT</td>
              <td><span class="status-badge status-in-progress">Đang tiến hành</span></td>
              <td>-</td>
              <td class="actions row-actions">
                <button type="button" title="View/Edit"><i class="fa-solid fa-edit"></i></button>
                <button type="button" title="Send Reminder"><i class="fa-solid fa-bell"></i></button>
              </td>
            </tr>
            <tr>
              <td>Q1 2025</td>
              <td>Trần Thị B</td>
              <td>Sales Executive</td>
              <td>Sales</td>
              <td><span class="status-badge status-completed">Đã hoàn thành</span></td>
              <td>2025-04-15</td>
              <td class="actions row-actions">
                <button type="button" title="View Details"><i class="fa-solid fa-eye"></i></button>
              </td>
            </tr>
            <tr>
              <td>Q2 2025</td>
              <td>Lê Văn C</td>
              <td>HR Specialist</td>
              <td>Human Resources</td>
              <td><span class="status-badge status-not-started">Chưa bắt đầu</span></td>
              <td>-</td>
              <td class="actions row-actions">
                <button type="button" title="Start Review"><i class="fa-solid fa-play"></i></button>
              </td>
            </tr>
            <tr>
              <td>Q1 2025</td>
              <td>Phạm Thị D</td>
              <td>Marketing Manager</td>
              <td>Sales</td>
              <td><span class="status-badge status-completed">Đã hoàn thành</span></td>
              <td>2025-04-10</td>
              <td class="actions row-actions">
                <button type="button" title="View Details"><i class="fa-solid fa-eye"></i></button>
              </td>
            </tr>
            <!-- Add more placeholder rows as needed -->
          </tbody>
        </table>
        <!-- Pagination (Optional) -->
        <!--
        <div class="pagination">
          <span class="disabled">&laquo;</span>
          <span class="current">1</span>
          <a href="#">&raquo;</a>
        </div>
        -->
      </div> <!-- End middle-content -->
      <!-- Bottom Navigation (Optional or adjust as needed) -->
      <div class="bottom-nav">
        <button type="button">Not Started</button>
        <button type="button">In Progress</button>
        <button type="button">Completed</button>
        <button type="button" class="active">All Reviews</button>
      </div>
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