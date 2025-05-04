<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="iytk87" class="middle-content"> <!-- Added wrapper for independent scrolling -->
        <h1>HR Management</h1>
        <h2 id="iqoww3">Employee List (All)</h2>
        <!-- Action Bar -->
        <div class="action-bar gjs-grid-row">
          <div class="filters gjs-grid-column">
            <select type="text" class="shadow-border">
              <option>Filter by Department</option>
              <option>IT</option>
              <option>Sales</option>
            </select>
            <select type="text" class="shadow-border">
              <option>Filter by Position</option>
              <option>Developer</option>
              <option>Manager</option>
            </select>
            <select type="text" class="shadow-border">
              <option>Filter by Status</option>
              <option>Active</option>
              <option>Inactive</option>
            </select>
          </div>
          <div class="search gjs-grid-column">
            <input type="text" placeholder="Search ID, Name..." class="shadow-border"/>
          </div>
          <div class="buttons gjs-grid-column">
            <button type="button" class="secondary"><i class="fa-solid fa-file-csv"></i> Import CSV</button>
            <button type="button"><i class="fa-solid fa-plus"></i> Add Employee</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th>Employee ID</th>
              <th>Full Name</th>
              <th>Designation</th>
              <th>Department</th>
              <th>Status</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>EMP/0001</td>
              <td>Nguyễn Văn A</td>
              <td>Developer</td>
              <td>IT</td>
              <td>Active</td>
              <td class="actions">
                <a href="#"><i class="fa-solid fa-eye"></i></a>
                <a href="#"><i class="fa-solid fa-edit"></i></a>
              </td>
            </tr>
            <tr>
              <td>EMP/0002</td>
              <td>Trần Thị B</td>
              <td>Tester</td>
              <td>IT</td>
              <td>Active</td>
              <td class="actions">
                <a href="#"><i class="fa-solid fa-eye"></i></a>
                <a href="#"><i class="fa-solid fa-edit"></i></a>
              </td>
            </tr>
            <tr>
              <td>EMP/0003</td>
              <td>Lê Văn C</td>
              <td>Manager</td>
              <td>Sales</td>
              <td>Left</td>
              <td class="actions">
                <a href="#"><i class="fa-solid fa-eye"></i></a>
                <a href="#"><i class="fa-solid fa-edit"></i></a>
              </td>
            </tr>
            <!-- Add more placeholder rows as needed -->
            <tr>
              <td>EMP/0004</td>
              <td>Phạm Thị D</td>
              <td>HR Executive</td>
              <td>Human Resources</td>
              <td>Active</td>
              <td class="actions">
                <a href="#"><i class="fa-solid fa-eye"></i></a>
                <a href="#"><i class="fa-solid fa-edit"></i></a>
              </td>
            </tr>
            <tr>
              <td>EMP/0005</td>
              <td>Hoàng Văn E</td>
              <td>Developer</td>
              <td>IT</td>
              <td>Active</td>
              <td class="actions">
                <a href="#"><i class="fa-solid fa-eye"></i></a>
                <a href="#"><i class="fa-solid fa-edit"></i></a>
              </td>
            </tr>
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
      <!-- Bottom Navigation -->
      <div class="bottom-nav">
        <button type="button" class="active">All Employees</button>
        <button type="button">Departments</button>
        <button type="button">Positions</button>
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