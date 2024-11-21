import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of not found files without the "vendor/" prefix
not_found_files = [
    "etc/displayconfig/display_id_4630947134992368258.xml",
    "etc/acdbdata/Mise_elus/Mise_elus_acdb_cal.acdb",
    "etc/acdbdata/Mise_elus/Mise_elus_workspaceFileXml.qwsp",
    "etc/camera/CFR_para_T_2x_V01.bin",
    "etc/camera/CFR_para_T_2x_V01_HD.bin",
    "etc/camera/CFR_para_T_2x_V01_SN.bin",
    "etc/camera/CFR_para_UW_V01.bin",
    "etc/camera/CFR_para_UW_V01_HD.bin",
    "etc/camera/CFR_para_UW_V01_SN.bin",
    "etc/camera/CFR_para_W_V01_HD.bin",
    "etc/camera/CFR_para_W_V01_SN.bin",
    "etc/camera/arcsat_3sat.bin",
    "etc/camera/com.xiaomi.dcal.wt.golden",
    "etc/camera/com.xiaomi.dcallite.wt.data",
    "etc/camera/com.xiaomi.dcallite.wu.data",
    "etc/camera/dualcam_bokeh_params.json",
    "etc/camera/eisoverridesettings.txt",
    "etc/camera/ellv.bin",
    "etc/camera/ellv_params.xml",
    "etc/camera/preview_bokeh_params_pro.json",
    "etc/camera/zeus_enhance_motiontuning.xml",
    "etc/camera/zeus_motiontuning.xml",
    "etc/display/qdcm_calib_data_xiaomi_38_0c_0a_cmd_mode_dsc_dsi_panel.json",
    "etc/mdss_dsi_l2_38_0c_0a_dsc_cmd_mi.xml",
    "etc/sensors/config/bu27030_0_back.json",
    "etc/sensors/config/fs203.json",
    "etc/sensors/config/gs1602.json",
    "etc/sensors/config/lsm6dso_0.json",
    "etc/sensors/config/sm8450_bu27030_0_back.json",
    "etc/sensors/config/sm8450_fs203.json",
    "etc/sensors/config/sm8450_gs1602.json",
    "etc/sensors/config/sm8450_lsm6dso_0.json",
    "etc/sensors/config/sm8450_sx933x_0.json",
    "etc/sensors/config/sm8450_tmd3719.json",
    "etc/sensors/config/sx933x_0.json",
    "etc/sensors/config/tmd3719.json",
    "etc/sensors/sensorDisplayMap.json",
    "etc/thermal-abnormal.conf",
    "etc/thermal-iec-4k.conf",
    "etc/thermal-iec-camera.conf",
    "etc/thermal-iec-chg-only.conf",
    "etc/thermal-iec-class0.conf",
    "etc/thermal-iec-huanji.conf",
    "etc/thermal-iec-mgame.conf",
    "etc/thermal-iec-navigation.conf",
    "etc/thermal-iec-nolimits.conf",
    "etc/thermal-iec-normal.conf",
    "etc/thermal-iec-per-class0.conf",
    "etc/thermal-iec-per-navigation.conf",
    "etc/thermal-iec-per-normal.conf",
    "etc/thermal-iec-per-video.conf",
    "etc/thermal-iec-phone.conf",
    "etc/thermal-iec-tgame.conf",
    "etc/thermal-iec-video.conf",
    "etc/thermal-iec-videochat.conf",
    "firmware/st_fts_l1.ftb",
    "firmware/stm_fts_production_limits.csv",
    "firmware/zeus_wide_bu24618_ois.coeff",
    "firmware/zeus_wide_bu24618_ois.mem",
    "firmware/zeus_wide_bu24618_ois.prog",
    "lib/rfsa/adsp/libmialgo_mc_bokeh_cdsp_skel.so",
    "lib/rfsa/adsp/libproxy_skel.so",
    "lib64/camera/com.qti.actuator.zeus_semco_imx707_ak7314_wide_actuator.so",
    "lib64/camera/com.qti.actuator.zeus_sunny_s5kjn1_dw9714_tele_actuator.so",
    "lib64/camera/com.qti.eeprom.zeus_ofilm_ov32b40_p24c64f_front_eeprom.so",
    "lib64/camera/com.qti.eeprom.zeus_semco_imx707_p24c128f_wide_eeprom.so",
    "lib64/camera/com.qti.eeprom.zeus_sunny_s5kjn1_bl24sa128b_ultra_eeprom.so",
    "lib64/camera/com.qti.eeprom.zeus_sunny_s5kjn1_gt24p128e_tele_eeprom.so",
    "lib64/camera/com.qti.ois.zeus_wide_bu24618_ois.so",
    "lib64/camera/com.qti.sensor.zeus_ofilm_ov32b40_front.so",
    "lib64/camera/com.qti.sensor.zeus_semco_imx707_wide.so",
    "lib64/camera/com.qti.sensor.zeus_sunny_s5kjn1_tele.so",
    "lib64/camera/com.qti.sensor.zeus_sunny_s5kjn1_ultra.so",
    "lib64/camera/com.qti.sensormodule.zeus_ofilm_ov32b40_front.bin",
    "lib64/camera/com.qti.sensormodule.zeus_semco_imx707_wide.bin",
    "lib64/camera/com.qti.sensormodule.zeus_sunny_s5kjn1_tele.bin",
    "lib64/camera/com.qti.sensormodule.zeus_sunny_s5kjn1_ultra.bin",
    "lib64/camera/com.qti.tuned.zeus_ofilm_ov32b40_front.bin",
    "lib64/camera/com.qti.tuned.zeus_semco_imx707_wide.bin",
    "lib64/camera/com.qti.tuned.zeus_sunny_s5kjn1_tele.bin",
    "lib64/camera/com.qti.tuned.zeus_sunny_s5kjn1_ultra.bin",
    "lib64/camera/components/com.xiaomi.node.smooth_transition.so",
    "lib64/hw/fingerprint.goodix_fod.default.so",
    "lib64/hw/fingerprint.goodix_fod6.default.so",
    "lib64/libarc_sat.so",
    "lib64/libarc_translate.so",
    "lib64/libarccali_data.so",
    "lib64/libarcsoft_dualcam_refocus_image.so",
    "lib64/libarcsoft_dualcam_refocus_video.so",
    "lib64/libarm_proxy_skel.so",
    "lib64/libdualcam_optical_zoom_control.so",
    "lib64/libdualcam_video_optical_zoom.so",
    "lib64/libgf_hal6.so",
    "lib64/libhvx_proxy_stub.so",
    "lib64/libmiStereoFactoryRemapBasicLib.so",
    "lib64/libmibokeh_mask.so",
    "lib64/libmiphone_capture_bokeh.so",
    "lib64/librmsclib1.so",
    "lib64/libtriplecam_optical_zoom_control.so",
    "lib64/libtriplecam_video_optical_zoom.so"
]

def find_file_in_dump(base_path, target_file):
    """
    Find the target file in the base_path.
    """
    logging.info(f"Searching for {target_file} in {base_path}")
    for root, dirs, files in os.walk(base_path):
        if target_file in files:
            found_file = os.path.join(root, target_file)
            logging.info(f"Found {target_file} at {found_file}")
            return found_file
    logging.warning(f"File {target_file} not found in {base_path}")
    return None

def update_vendor_mk(vendor_mk_path, base_path):
    """
    Update the ingres-vendor.mk file with the correct paths.
    """
    logging.info(f"Reading ingres-vendor.mk file from {vendor_mk_path}")
    with open(vendor_mk_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    changes = []
    for line in lines:
        if line.strip().startswith("PRODUCT_COPY_FILES"):
            parts = line.split()
            source_file = parts[1].strip()
            logging.info(f"Processing line: {line.strip()}")
            if source_file in not_found_files:
                new_source_file = find_file_in_dump(base_path, os.path.basename(source_file))
                if new_source_file:
                    parts[1] = new_source_file
                    updated_line = ' '.join(parts) + '\n'
                    changes.append((line.strip(), updated_line.strip()))
                    updated_lines.append(updated_line)
                    logging.info(f"Updated line: {updated_line.strip()}")
                else:
                    updated_lines.append(line)
                    logging.warning(f"File {source_file} not found, keeping original line: {line.strip()}")
            else:
                updated_lines.append(line)
                logging.info(f"Keeping original line: {line.strip()}")
        else:
            updated_lines.append(line)
            logging.info(f"Keeping original line: {line.strip()}")

    # Display the changes and ask for confirmation
    print("Proposed changes to ingres-vendor.mk:")
    for old, new in changes:
        print(f"Old: {old}")
        print(f"New: {new}")
        print("-" * 40)

    confirm = input("Do you want to apply these changes? (y/n): ")
    if confirm.lower() == 'y':
        logging.info("Applying changes to ingres-vendor.mk")
        with open(vendor_mk_path, 'w') as file:
            file.writelines(updated_lines)
        print("Vendor MK file updated successfully.")
    else:
        logging.info("Changes were not applied.")
        print("Changes were not applied.")

if __name__ == "__main__":
    vendor_dump_path = "~/lineage/device/xiaomi/ingres/vendor/ingres/vendor"  # Update this path
    vendor_mk_path = "ingres-vendor.mk"  # Update this path

    logging.info(f"Starting script with vendor dump path: {vendor_dump_path} and ingres-vendor.mk path: {vendor_mk_path}")
    update_vendor_mk(vendor_mk_path, vendor_dump_path)
