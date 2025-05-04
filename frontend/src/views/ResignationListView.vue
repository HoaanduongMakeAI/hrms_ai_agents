<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="ivhhhh-5" class="middle-content">
        <!-- Action Bar -->
        <div class="action-bar gjs-grid-row">
          <div class="filters gjs-grid-column">
            <label for="status-filter-2">Status:</label> <!-- Changed id -->
            <select type="text" id="status-filter-2" class="shadow-border">
              <option value="">All</option>
              <option value="pending">Chờ duyệt</option>
              <option value="approved">Đã duyệt</option>
              <option value="rejected">Đã từ chối</option>
            </select>
            <label for="dept-filter-2">Department:</label> <!-- Changed id -->
            <select type="text" id="dept-filter-2" class="shadow-border">
              <option value="">All</option>
              <option value="it">IT</option>
              <option value="sales">Sales</option>
              <option value="hr">Human Resources</option>
            </select>
          </div>
          <div class="search gjs-grid-column">
            <input type="text" placeholder="Search by Employee Name..." class="shadow-border"/>
          </div>
          <div class="buttons gjs-grid-column">
            <button type="button" class="secondary"><i class="fa-solid fa-filter"></i> Apply Filters</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th>Employee Name</th>
              <th>Position</th>
              <th>Department</th>
              <th>Submission Date</th>
              <th>Requested Last Day</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Nguyễn Văn A</td>
              <td>Software Engineer</td>
              <td>IT</td>
              <td>2025-04-28</td>
              <td>2025-05-15</td>
              <td><span class="status-badge status-pending">Chờ duyệt</span></td>
              <td class="actions">
                <a href="#" title="View Details"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Process"><i class="fa-solid fa-cogs"></i></a> <!-- Placeholder for Process action -->
              </td>
            </tr>
            <tr>
              <td>Trần Thị B</td>
              <td>Sales Executive</td>
              <td>Sales</td>
              <td>2025-04-27</td>
              <td>2025-05-10</td>
              <td><span class="status-badge status-approved">Đã duyệt</span></td>
              <td class="actions">
                <a href="#" title="View Details"><i class="fa-solid fa-eye"></i></a>
              </td>
            </tr>
            <tr>
              <td>Lê Văn C</td>
              <td>HR Specialist</td>
              <td>Human Resources</td>
              <td>2025-04-29</td>
              <td>2025-05-20</td>
              <td><span class="status-badge status-pending">Chờ duyệt</span></td>
              <td class="actions">
                <a href="#" title="View Details"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Process"><i class="fa-solid fa-cogs"></i></a>
              </td>
            </tr>
            <tr>
              <td>Phạm Thị D</td>
              <td>Marketing Manager</td>
              <td>Sales</td>
              <td>2025-04-25</td>
              <td>2025-05-05</td>
              <td><span class="status-badge status-rejected">Đã từ chối</span></td>
              <td class="actions">
                <a href="#" title="View Details"><i class="fa-solid fa-eye"></i></a>
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
        <button type="button">Pending</button>
        <button type="button">Approved</button>
        <button type="button">Rejected</button>
        <button type="button" class="active">All Requests</button>
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