<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="ivhhhh" class="middle-content"> <!-- Scroll wrapper -->
        <h1>HR Management</h1>
        <h2 id="ikdkpn">Department List</h2>
        <!-- Action Bar -->
        <div class="action-bar gjs-grid-row">
          <div class="search gjs-grid-column">
            <input type="text" placeholder="Search Departments..." class="shadow-border"/>
          </div>
          <div class="buttons gjs-grid-column">
            <button type="button"><i class="fa-solid fa-plus"></i> Add Department</button>
          </div>
        </div>
        <!-- Data Table -->
        <table class="data-table shadow-border">
          <thead>
            <tr>
              <th>Department Name</th>
              <th>Head of Department</th>
              <th>Employee Count</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>IT</td>
              <td>Trần Văn D</td>
              <td>15</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
              </td>
            </tr>
            <tr>
              <td>Sales</td>
              <td>Nguyễn Thị E</td>
              <td>25</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
              </td>
            </tr>
            <tr>
              <td>Human Resources</td>
              <td>Lê Thị F</td>
              <td>5</td>
              <td class="actions">
                <a href="#" title="View"><i class="fa-solid fa-eye"></i></a>
                <a href="#" title="Edit"><i class="fa-solid fa-edit"></i></a>
                <a href="#" title="Delete" class="delete"><i class="fa-solid fa-trash"></i></a>
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
      <!-- Bottom Navigation -->
      <div class="bottom-nav">
        <button type="button">All Employees</button>
        <button type="button" class="active">Departments</button>
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