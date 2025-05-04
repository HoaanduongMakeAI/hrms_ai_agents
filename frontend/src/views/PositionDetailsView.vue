<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="iiyyq8x" class="middle-content"> <!-- Scroll wrapper -->
        <h1 id="ia5napd">HR Management</h1>
        <h2 id="iqj6ez8">Position Details (Add/Edit)</h2>
        <!-- Position Form -->
        <div class="position-form">
          <!-- Position Details -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-id-badge"></i> Position Information</h3>
            <div class="form-grid gjs-grid-row">
              <div class="form-group gjs-grid-column">
                <label for="designation_name">Position Name (Designation)</label>
                <input type="text" id="designation_name" name="designation_name" value="Developer" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="description-2">Description</label> <!-- Changed id -->
                <textarea id="description-2" name="description" class="shadow-border">Software Development and Maintenance...</textarea>
              </div>
            </div>
          </div>
          <!-- Employee List Section -->
          <div id="imaondg" class="form-section employee-list-section shadow-border">
            <h4><i class="fa-solid fa-users"></i> Employees with this Position</h4> <!-- Corrected icon -->
            <div class="employee-list-actions">
              <button type="button"><i class="fa-solid fa-user-plus"></i> Assign Employee to Position</button>
            </div>
            <table class="data-table shadow-border">
              <thead>
                <tr>
                  <th>Employee ID</th>
                  <th>Full Name</th>
                  <th>Department</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>EMP/0001</td>
                  <td>Nguyễn Văn A</td>
                  <td>IT</td>
                  <td class="actions">
                    <a href="#" title="Remove from Position"><i class="fa-solid fa-user-minus"></i></a>
                  </td>
                </tr>
                <tr>
                  <td>EMP/0005</td>
                  <td>Hoàng Văn E</td>
                  <td>IT</td>
                  <td class="actions">
                    <a href="#" title="Remove from Position"><i class="fa-solid fa-user-minus"></i></a>
                  </td>
                </tr>
                <!-- Add more placeholder rows -->
              </tbody>
            </table>
          </div>
          <!-- Form Actions -->
          <div class="form-actions gjs-grid-row">
            <button type="button" class="danger"><i class="fa-solid fa-trash"></i> Delete Position</button>
            <button type="button" class="secondary"><i class="fa-solid fa-times"></i> Cancel</button>
            <button type="button" class="primary"><i class="fa-solid fa-save"></i> Save</button>
          </div>
        </div>
      </div> <!-- End middle-content -->
      <!-- Bottom Navigation -->
      <div class="bottom-nav">
        <button type="button">All Employees</button>
        <button type="button">Departments</button>
        <button type="button" class="active">Positions</button>
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