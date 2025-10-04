# Security Policy

## Supported Versions

Only maps published in the official ZombieRool Maps repository are verified and safe.

| Source | Supported |
|--------|-----------|
| Official GitHub Repo | ✅ Yes |
| Third-party mirrors | ❌ No |
| Discord file uploads | ⚠️ Use caution |

## Security Measures

### For Map Publishers

All maps published in this repository undergo these security checks:

1. **File Size Limit**: Max 500 MB per file
2. **Domain Whitelist**: Only GitHub domains are accepted
3. **SHA-256 Checksums**: Verify file integrity (optional but recommended)
4. **Manual Review**: All maps are tested before publication

### For Players

The mod includes these protections:

- ✅ URL validation (only GitHub domains)
- ✅ File size limits (500 MB max)
- ✅ Zip Slip protection
- ✅ Timeout protection (max 5 min per download)
- ✅ Automatic resource pack prompts

## Reporting a Vulnerability

If you discover a security issue:

1. **DO NOT** open a public issue
2. Contact us via Discord: https://discord.gg/HGv2r44hXM
3. Email: c5039959@gmail.com

Please include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will respond within 48 hours.

## Known Limitations

- No antivirus scanning (resource packs are user content)
- No runtime validation of textures/sounds
- Checksums are optional (maintainer must add them)

## Safe Usage Guidelines

### For Players

✅ **DO**:
- Download only from the in-game downloader
- Report suspicious maps
- Keep your game updated

❌ **DON'T**:
- Download from untrusted sources
- Share your account credentials
- Modify `maps.json` manually

### For Map Creators

✅ **DO**:
- Test your maps thoroughly
- Use appropriate content warnings
- Include a README with your map
- Generate SHA-256 checksums

❌ **DON'T**:
- Include executable files
- Use offensive content
- Exceed 500 MB file size
- Include malicious textures (flashing lights, etc.)

## Checksum Verification

To verify a map's integrity:

```bash
# Linux/Mac
sha256sum your_map.zip

# Windows (PowerShell)
Get-FileHash your_map.zip -Algorithm SHA256
```

Compare the output with the `sha256` field in `maps.json`.

## License

All maps in this repository are provided "AS IS" without warranty. By downloading, you accept the risks associated with user-generated content.

## Contact

- Discord: https://discord.gg/HGv2r44hXM
- GitHub Issues: For non-security bugs only
- Email: c5039959@gmail.com

---

**Last Updated**: 2025-10-04  
**Maintained By**: Cryo60